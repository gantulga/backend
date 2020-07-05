from rest_framework import serializers
from .models import Item_transfer, Commodity, Product, Store, Item_transfer_type, Item_balance
from django.contrib.auth import get_user_model
from datetime import datetime
from structure_app.serializers import UsersSerializer
import json

User = get_user_model()


class ItemTransfersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_transfer
        fields = '__all__'
        # depth = 1

    def create(self, validated_data):
        transfer = Item_transfer.objects.create(**validated_data)
        if transfer:
            if validated_data['fr_division']:
                # PRODUCT
                if validated_data['fr_client'] and validated_data['fr_user'] == None and validated_data['product']:
                    fr_last_one = Item_balance.objects.filter(product=validated_data['product'],
                                                              client=validated_data['fr_client']).order_by('-id')[:1]
                if validated_data['fr_user'] and validated_data['fr_client'] == None and validated_data['product']:
                    fr_last_one = Item_balance.objects.filter(product=validated_data['product'],
                                                              user=validated_data['fr_user']).order_by('-id')[:1]

                if validated_data['to_client'] and validated_data['to_user'] == None and validated_data['product']:
                    to_last_one = Item_balance.objects.filter(product=validated_data['product'],
                                                              client=validated_data['to_client']).order_by('-id')[:1]
                if validated_data['to_user'] and validated_data['to_client'] == None and validated_data['product']:
                    to_last_one = Item_balance.objects.filter(product=validated_data['product'],
                                                              user=validated_data['to_user']).order_by('-id')[:1]
                # COMMODITY
                if validated_data['fr_client'] and validated_data['fr_user'] == None and validated_data['commodity']:
                    fr_last_one = Item_balance.objects.filter(commodity=validated_data['commodity'],
                                                              client=validated_data['fr_client']).order_by('-id')[:1]
                if validated_data['fr_user'] and validated_data['fr_client'] == None and validated_data['commodity']:
                    fr_last_one = Item_balance.objects.filter(commodity=validated_data['commodity'],
                                                              user=validated_data['fr_user']).order_by('-id')[:1]

                if validated_data['to_client'] and validated_data['to_user'] == None and validated_data['commodity']:
                    to_last_one = Item_balance.objects.filter(commodity=validated_data['commodity'],
                                                              client=validated_data['to_client']).order_by('-id')[:1]
                if validated_data['to_user'] and validated_data['to_client'] == None and validated_data['commodity']:
                    to_last_one = Item_balance.objects.filter(commodity=validated_data['commodity'],
                                                              user=validated_data['to_user']).order_by('-id')[:1]

                if fr_last_one:
                    # Umnu n record bsan uyed
                    fr_last_one_quantity = fr_last_one[0].quantity
                    fr_last_one_size = fr_last_one[0].size
                    if validated_data['quantity']:
                        quantity = fr_last_one_quantity - \
                            validated_data['quantity']
                    else:
                        quantity = None

                    if validated_data['size']:
                        size = fr_last_one_size - validated_data['size']
                    else:
                        size = None

                    balance = Item_balance.objects.get(
                        pk=fr_last_one[0].id)
                    balance.updated_by = validated_data['created_by']
                    balance.size = size
                    balance.quantity = quantity
                    balance.save()

                if to_last_one:
                    # Umnu n record bsan uyed
                    to_last_one_quantity = to_last_one[0].quantity
                    to_last_one_size = to_last_one[0].size
                    if validated_data['quantity']:
                        quantity = to_last_one_quantity + \
                            validated_data['quantity']
                    else:
                        quantity = None

                    if validated_data['size']:
                        size = to_last_one_size + validated_data['size']
                    else:
                        size = None

                    balance = Item_balance.objects.get(
                        pk=to_last_one[0].id)
                    balance.updated_by = validated_data['created_by']
                    balance.size = size
                    balance.quantity = quantity
                    balance.save()
                else:
                    # Umnu n record bgaagui uyed
                    balance = Item_balance.objects.create(
                        created_by=validated_data['created_by'], quantity=validated_data['quantity'], size=validated_data['size'], client=validated_data['to_client'], division=validated_data['to_division'], product=validated_data['product'], commodity=validated_data['commodity'], user=validated_data['to_user'])

            else:
                # umnuh balanciig shalgaj bn
                if validated_data['product']:
                    last_one = Item_balance.objects.filter(product=validated_data['product'],
                                                           client=validated_data['to_client']).order_by('-id')[:1]

                if validated_data['commodity']:
                    last_one = Item_balance.objects.filter(commodity=validated_data['commodity'],
                                                           client=validated_data['to_client']).order_by('-id')[:1]

                if last_one:
                    # Umnu n record bsan uyed
                    if validated_data['size']:
                        last_one_size = last_one[0].size
                        size = int(validated_data['size']) + int(last_one_size)
                    else:
                        size = None

                    if validated_data['quantity']:
                        last_one_quantity = last_one[0].quantity
                        quantity = int(
                            validated_data['quantity']) + int(last_one_quantity)
                    else:
                        quantity = None

                    balance = Item_balance.objects.get(pk=last_one[0].id)
                    balance.updated_by = validated_data['created_by']
                    balance.size = size
                    balance.quantity = quantity
                    balance.save()
                else:
                    # Umnu n record bgaagui uyed
                    if validated_data['size']:
                        size = int(validated_data['size'])
                    else:
                        size = None

                    if validated_data['quantity']:
                        quantity = int(
                            validated_data['quantity'])
                    else:
                        quantity = None

                    balance = Item_balance.objects.create(
                        created_by=validated_data['created_by'], quantity=quantity, size=size, client=validated_data['to_client'], division=validated_data['to_division'], commodity=validated_data['commodity'], product=validated_data['product'], user=validated_data['to_user'])

        return transfer


class CommoditiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodity
        fields = '__all__'
        # depth = 1


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # depth = 1


class BalancesSerializer(serializers.ModelSerializer):
    # user = UsersSerializer(many=False, read_only=True)

    class Meta:
        model = Item_balance
        # fields = ['id', 'client', 'commodity',
        #           'division', 'product', 'quantity', 'size', 'user']
        fields = '__all__'
        # depth = 1


class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'
        # depth = 1


class TransferTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_transfer_type
        fields = '__all__'
        # depth = 1


class ClientItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_balance
        fields = '__all__'
        depth = 1


class DivisionItemBalancesSerializer(serializers.ModelSerializer):
    commodity = CommoditiesSerializer(read_only=True, many=False)
    product = ProductsSerializer(read_only=True, many=False)

    class Meta:
        model = Item_balance
        fields = ['id', 'quantity', 'size',
                  'division', 'client', 'user', 'commodity', 'product']
        # depth = 1
