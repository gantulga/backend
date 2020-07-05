from rest_framework import serializers
from hotel.models import Hotel_client_log, Hotel_client_item
from structure_app.models import Client, Division, Shift_work
from product_app.models import Product, Item_transfer, Item_transfer_type, Item_balance
from payment_app.models import Order, Order_detial, Payment
from structure_app.serializers import CustomersSerializer, ClientsSerializer
from financial_app.models import Money_transfer, Currency, Money_transfer_type, Wallet
import json
from django.contrib.auth import get_user_model
User = get_user_model()


# Hotel_client_log Serializer


class HotelClientLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel_client_log
        fields = '__all__'
        depth = 1


class HotelClientLogsSerializer2(serializers.ModelSerializer):
    # RoomDiv ungu solihod ashiglagdah api
    class Meta:
        model = Hotel_client_log
        fields = '__all__'


class HotelProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class HotelClientItemsSerializers(serializers.ModelSerializer):
    product = HotelProductsSerializers(read_only=True)

    class Meta:
        model = Hotel_client_item
        fields = ('product', 'quantity')


class ItemBalancesSerializers(serializers.ModelSerializer):
    product = HotelProductsSerializers(read_only=True)

    class Meta:
        model = Item_balance
        fields = ('product', 'quantity')


class HotelRoomsSerializer(serializers.ModelSerializer):
    client_items = HotelClientItemsSerializers(read_only=True, many=True)
    item_balances = ItemBalancesSerializers(read_only=True, many=True)
    client_products = HotelProductsSerializers(read_only=True, many=True)

    class Meta:
        model = Client
        fields = ['id', 'number', 'description',
                  'client_products', 'client_items', 'free', 'clean', 'minibarFull', 'client_items', 'item_balances']

    def update(self, instance, validated_data):
        # instance.username = validated_data.get('username', instance.username)
        # instance.email = validated_data.get('email', instance.email)
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        if validated_data.get('free') != None:
            Hotel_client_log.objects.create(
                choices_type=1, client=instance, value="out")
        if validated_data.get('clean') != None:
            Hotel_client_log.objects.create(
                choices_type=3, client=instance, value="c")
        if validated_data.get('minibarFull') != None:
            Hotel_client_log.objects.create(
                choices_type=4, client=instance, value="r")
        return instance


class HotelPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class HotelPaymentsSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        depth = 1


class HotelOrderDetialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_detial
        fields = '__all__'

    def validate(self, data):
        fr_date = data['fr_date']
        to_date = data['to_date']
        fr_check = Order_detial.objects.filter(
            fr_date__gte=fr_date, fr_date__lte=to_date, client=data['client'], is_deleted=False)
        to_check = Order_detial.objects.filter(
            to_date__gte=fr_date, to_date__lte=to_date, client=data['client'], is_deleted=False)
        if fr_check or to_check:
            raise serializers.ValidationError(
                {"date_error": "Энэ өрөөнд тухайн цагт захиалга байгаа тул захиалах боломжгүй байна."}
            )
        else:
            Hotel_client_log.objects.create(
                choices_type=1, client=data['client'], value="in")
            Hotel_client_log.objects.create(
                choices_type=3, client=data['client'], value="d")

            client = Client.objects.get(pk=data['client'].id)
            client.free = False
            client.clean = False
            client.save()
        return data

    def create(self, validated_data):
        division = Division.objects.get(pk=3)
        last_notFinished_shiftWork = Shift_work.objects.filter(
            finished=False, division=division).order_by('-id')[0]
        if last_notFinished_shiftWork:
            detial = Order_detial.objects.create(
                **validated_data, shift_work=last_notFinished_shiftWork)
            return detial


# class HotelOrdersSerializer(serializers.ModelSerializer):
#     payments = HotelPaymentsSerializer(many=True)
#     customer = CustomersSerializer()

#     class Meta:
#         model = Order
#         fields = ['id', 'created_at', 'updated_at', 'amount', 'required_date', 'is_now',
#                   'status', 'client', 'created_by', 'customer', 'division', 'updated_by', 'payments']

# Order deer mini bar product nemeh uyer ashiglagdah Serializer
class HotelOrderDetialsSerializer2(serializers.ModelSerializer):

    class Meta:
        model = Order_detial
        #fields = ['created_at', 'updated_at', 'quantity', 'fr_date', 'to_date', 'created_by', 'order', 'product', 'updated_by', 'subtotal', 'deleted_date', 'is_deleted', 'why_deleted', 'client']
        fields = '__all__'

    def create(self, validated_data):
        division = Division.objects.get(pk=3)
        last_notFinished_shiftWork = Shift_work.objects.filter(
            finished=False, division=division).order_by('-id')[0]
        if last_notFinished_shiftWork:
            detial = Order_detial.objects.create(
                **validated_data, shift_work=last_notFinished_shiftWork)
            if detial:
                itemTransferType = Item_transfer_type.objects.get(pk=3)
                itemTransfer = Item_transfer.objects.create(product=validated_data['product'],
                                                            fr_client=validated_data['fr_client'], quantity=validated_data['quantity'], created_by=validated_data['created_by'], order_detial=detial, item_transfer_type=itemTransferType)
                if itemTransfer:
                    fr_client_item_balance = Item_balance.objects.filter(
                        product=validated_data['product'], client=validated_data['fr_client']).order_by('-id')[:1]

                    if fr_client_item_balance:
                        balance = Item_balance.objects.get(
                            pk=fr_client_item_balance[0].id)
                        quantity = balance.quantity - \
                            validated_data['quantity']
                        balance.updated_by = validated_data['created_by']
                        balance.quantity = quantity
                        balance.save()
            return detial


class HotelOrderDetialsSerializer3(serializers.ModelSerializer):
    class Meta:
        model = Order_detial
        fields = '__all__'
        depth = 1


class UnderpaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'created_at', 'updated_at', 'amount', 'required_date', 'is_now',
                  'status', 'client', 'customer', 'division', 'updated_by', 'payments']
        depth = 1


class HotelOrdersNewHotelSerializer(serializers.ModelSerializer):
    payments = HotelPaymentsSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'updated_at', 'amount', 'required_date', 'is_now',
                  'status', 'client', 'created_by', 'customer', 'division', 'updated_by', 'payments']

    def validate(self, data):
        fr_date = self.context['request'].data['fr_date']
        to_date = self.context['request'].data['to_date']
        fr_check = Order_detial.objects.filter(
            fr_date__gte=fr_date, fr_date__lte=to_date, client=data['client'], is_deleted=False)
        to_check = Order_detial.objects.filter(
            to_date__gte=fr_date, to_date__lte=to_date, client=data['client'], is_deleted=False)
        if fr_check or to_check:
            raise serializers.ValidationError(
                {"date_error": "Энэ өрөөнд тухайн цагт захиалга байгаа тул захиалах боломжгүй байна."}
            )
        return data

    def create(self, validated_data):
        payments_data = validated_data.pop('payments')
        division = Division.objects.get(pk=3)
        last_notFinished_shiftWork = Shift_work.objects.filter(
            finished=False, division=division).order_by('-id')[0]
        if last_notFinished_shiftWork:
            order = Order.objects.create(
                **validated_data, shift_work=last_notFinished_shiftWork)
            for payment in payments_data:
                payment = dict(payment)
                if payment["amount"] != 0:
                    payment1 = Payment.objects.create(
                        **payment, shift_work=last_notFinished_shiftWork, division=division)

                    hotelpos = Wallet.objects.get(pk=4)
                    loungepos = Wallet.objects.get(pk=5)
                    if payment['wallet'] != hotelpos and payment['wallet'] != loungepos:
                        currency = Currency.objects.get(pk=1)
                        money_transfer_type = Money_transfer_type.objects.get(
                            pk=1)
                        money_transfer = Money_transfer.objects.create(
                            created_by=payment['created_by'], amount=payment['amount'], currency=currency, customer=validated_data['customer'], division=validated_data['division'], money_transfer_type=money_transfer_type, payment=payment1, to_wallet=payment['wallet'], description="Зочид буудлаас орж ирсэн орлогын гүйлгээ.")
                    payment1.payments.add(order)
            return order

    def update(self, instance, validated_data):
        if validated_data.get('payments') != None and validated_data.get('amount'):

            division = Division.objects.get(pk=3)
            last_notFinished_shiftWork = Shift_work.objects.filter(
                finished=False, division=division).order_by('-id')[0]
            if last_notFinished_shiftWork:
                payments_data = validated_data.pop('payments')
                instance.amount = validated_data.get("amount", instance.amount)
                instance.status = validated_data.get("status", instance.status)
                instance.updated_at = validated_data.get(
                    "updated_at", instance.updated_at)
                instance.updated_by = validated_data.get(
                    "updated_by", instance.updated_by)
                instance.save()
                for payment in payments_data:
                    payment = dict(payment)
                    if payment["amount"] != 0:
                        payment1 = Payment.objects.create(
                            **payment, shift_work=last_notFinished_shiftWork, created_at=validated_data.get(
                                "confirmed_by"), division=division)
                        hotelpos = Wallet.objects.get(pk=4)
                        loungepos = Wallet.objects.get(pk=5)
                        if payment['wallet'] != hotelpos and payment['wallet'] != loungepos:
                            currency = Currency.objects.get(pk=1)
                            money_transfer_type = Money_transfer_type.objects.get(
                                pk=1)
                            money_transfer = Money_transfer.objects.create(
                                created_by=instance.created_by, amount=payment['amount'], currency=currency, customer=instance.customer, division=instance.division, money_transfer_type=money_transfer_type, payment=payment1, to_wallet=payment['wallet'], description="Зочид буудлаас орж ирсэн орлогын гүйлгээ.")
                        payment1.payments.add(instance)

        if validated_data.get('status'):
            instance.status = validated_data.get("status", instance.status)
            instance.save()
        return instance


class HotelOrdersSerializer(serializers.ModelSerializer):
    payments = HotelPaymentsSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'updated_at', 'amount', 'required_date', 'is_now',
                  'status', 'client', 'created_by', 'customer', 'division', 'updated_by', 'payments']

    def create(self, validated_data):
        payments_data = validated_data.pop('payments')
        division = Division.objects.get(pk=3)
        last_notFinished_shiftWork = Shift_work.objects.filter(
            finished=False, division=division).order_by('-id')[0]
        if last_notFinished_shiftWork:
            order = Order.objects.create(
                **validated_data, shift_work=last_notFinished_shiftWork)
            for payment in payments_data:
                payment = dict(payment)
                if payment["amount"] != 0:
                    payment1 = Payment.objects.create(
                        **payment, shift_work=last_notFinished_shiftWork, division=division)
                    hotelpos = Wallet.objects.get(pk=4)
                    loungepos = Wallet.objects.get(pk=5)
                    if payment['wallet'] != hotelpos and payment['wallet'] != loungepos:
                        currency = Currency.objects.get(pk=1)
                        money_transfer_type = Money_transfer_type.objects.get(
                            pk=1)
                        money_transfer = Money_transfer.objects.create(
                            created_by=payment['created_by'], amount=payment['amount'], currency=currency, customer=validated_data['customer'], division=validated_data['division'], money_transfer_type=money_transfer_type, payment=payment1, to_wallet=payment['wallet'], description="Зочид буудлаас орж ирсэн орлогын гүйлгээ.")
                    payment1.payments.add(order)
            return order

    def update(self, instance, validated_data):
        if validated_data.get('payments') != None and validated_data.get('amount'):

            division = Division.objects.get(pk=3)
            last_notFinished_shiftWork = Shift_work.objects.filter(
                finished=False, division=division).order_by('-id')[0]
            if last_notFinished_shiftWork:
                payments_data = validated_data.pop('payments')
                instance.amount = validated_data.get("amount", instance.amount)
                instance.status = validated_data.get("status", instance.status)
                instance.updated_at = validated_data.get(
                    "updated_at", instance.updated_at)
                instance.updated_by = validated_data.get(
                    "updated_by", instance.updated_by)
                instance.save()
                for payment in payments_data:
                    payment = dict(payment)
                    if payment["amount"] != 0:
                        payment1 = Payment.objects.create(
                            **payment, shift_work=last_notFinished_shiftWork, created_at=validated_data.get(
                                "confirmed_by"), division=division)
                        hotelpos = Wallet.objects.get(pk=4)
                        loungepos = Wallet.objects.get(pk=5)
                        if payment['wallet'] != hotelpos and payment['wallet'] != loungepos:
                            currency = Currency.objects.get(pk=1)
                            money_transfer_type = Money_transfer_type.objects.get(
                                pk=1)
                            money_transfer = Money_transfer.objects.create(
                                created_by=instance.created_by, amount=payment['amount'], currency=currency, customer=instance.customer, division=instance.division, money_transfer_type=money_transfer_type, payment=payment1, to_wallet=payment['wallet'], description="Зочид буудлаас орж ирсэн орлогын гүйлгээ.")
                        payment1.payments.add(instance)

        if validated_data.get('status'):
            instance.status = validated_data.get("status", instance.status)
            instance.save()
        return instance


class HotelOrdersSerializer2(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'updated_at', 'amount', 'required_date', 'is_now',
                  'status', 'client', 'created_by', 'customer', 'division', 'updated_by', 'payments', 'order_detials']
        depth = 2


class HotelOrdersSerializer3(serializers.ModelSerializer):
    payments = HotelPaymentsSerializer2(many=True)
    order_detials = HotelOrderDetialsSerializer3(many=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'updated_at', 'amount', 'required_date', 'is_now',
                  'status', 'client', 'created_by', 'customer', 'division', 'updated_by', 'payments', 'order_detials']
