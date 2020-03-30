from rest_framework import serializers
from hotel.models import Hotel_client_log, Hotel_client_item
from structure_app.models import Client
from product_app.models import Product

# Hotel_client_log Serializer


class HotelClientLogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel_client_log
        fields = '__all__'


class HotelProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'cost')


class HotelClientItemsSerializers(serializers.ModelSerializer):
    product = HotelProductsSerializers(read_only=True)

    class Meta:
        model = Hotel_client_item
        fields = ('product', 'quantity')


class HotelRoomsSerializer(serializers.ModelSerializer):
    client_products = HotelProductsSerializers(read_only=True, many=True)
    client_items = HotelClientItemsSerializers(read_only=True, many=True)

    class Meta:
        model = Client
        fields = ['id', 'number', 'description',
                  'client_products', 'client_items']
