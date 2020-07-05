from rest_framework import serializers
from .models import Configuration_value, Customer, Division, Client, Shift_work
from payment_app.models import Order, Order_detial, Payment
from product_app.models import Item_balance, Item_balance_log
from financial_app.models import Wallet, Money_transfer, Money_transfer_type, Currency
from django.contrib.auth.models import User

# Settings Serializer


class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration_value
        fields = '__all__'


class CustomersSerializer(serializers.ModelSerializer):
    mobile = serializers.IntegerField(
        required=False, allow_null=True)
    email = serializers.CharField(
        required=False, allow_null=True, allow_blank=True)
    address = serializers.CharField(
        required=False, allow_null=True, allow_blank=True)

    class Meta:
        model = Customer
        fields = '__all__'


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'is_superuser', 'username', 'first_name', 'last_name',
                  'email', 'is_staff', 'is_active', 'date_joined', 'groups', 'divisions']


class DivisionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ShiftWorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shift_work
        fields = '__all__'

    def create(self, validated_data):
        shift_work = Shift_work.objects.create(**validated_data)
        return shift_work

    def update(self, instance, validated_data):
        instance.worker_confirm = validated_data.get(
            'worker_confirm', instance.worker_confirm)
        instance.controller_confirm = validated_data.get(
            'controller_confirm', instance.controller_confirm)
        instance.finished = validated_data.get('finished', instance.finished)
        instance.controller = validated_data.get(
            'controller', instance.controller)
        instance.created_by = validated_data.get(
            'created_by', instance.created_by)
        instance.division = validated_data.get(
            'division', instance.division)
        instance.worker = validated_data.get(
            'worker', instance.worker)
        instance.save()
        if validated_data.get('finished') == True:
            poss = Wallet.objects.filter(division=instance.division)
            if poss:
                for pos in poss:
                    payments = Payment.objects.filter(
                        shift_work=instance, wallet=pos)
                    if payments:
                        total_amount = 0
                        for payment in payments:
                            total_amount = total_amount + payment.amount
                        description = instance.division.name + "-ын ПОС төхөөрөмжөөс орж ирсэн орлого."
                        transfer_fee = pos.transfer_fee/100 * total_amount
                        amount = total_amount - transfer_fee
                        to_wallet = Wallet.objects.get(pk=3)
                        money_transfer_type = Money_transfer_type.objects.get(
                            pk=1)
                        currency = Currency.objects.get(pk=1)
                        pos_money_transfer = Money_transfer.objects.create(
                            description=description, transfer_fee=transfer_fee, amount=amount, created_by=instance.created_by, currency=currency, division=instance.division, money_transfer_type=money_transfer_type, fr_wallet=pos, to_wallet=to_wallet)
                        if pos_money_transfer:
                            print("POS-ын гүйлгээ амжилттай үүслээ.")

            item_balances = Item_balance.objects.filter(
                division=instance.division)
            for item in item_balances:
                if item.commodity and item.product == None:
                    # Commodity
                    Item_balance_log.objects.create(
                        created_by=validated_data.get('created_by'),
                        size=item.size,
                        commodity=item.commodity,
                        client=item.client,
                        division=item.division,
                        shift_work=instance,
                        user=validated_data.get('worker')
                    )
                elif item.commodity == None and item.product:
                    # Product
                    Item_balance_log.objects.create(
                        created_by=validated_data.get('created_by'),
                        quantity=item.quantity,
                        product=item.product,
                        client=item.client,
                        division=item.division,
                        shift_work=instance,
                        user=validated_data.get('worker')
                    )
        return instance
