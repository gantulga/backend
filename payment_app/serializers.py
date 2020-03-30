from rest_framework import serializers
from .models import Order, Order_detial, Order_payments, Payment
from product_app.models import Product
from financial_app.models import Wallet


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class OrderDetialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_detial
        fields = '__all__'

    def validate(self, data):
        fr_date = data.pop('fr_date')
        to_date = data.pop('to_date')
        fr_check = Order_detial.objects.filter(
            fr_date__gte=fr_date, fr_date__lte=to_date, client=data['client'])
        to_check = Order_detial.objects.filter(
            to_date__gte=fr_date, to_date__lte=to_date, client=data['client'])
        if fr_check or to_check:
            raise serializers.ValidationError(
                {"date_error": "Энэ өрөөнд тухайн цагт захиалга байгаа тул захиалах боломжгүй байна."}
            )
        return data


class OrdersSerializer(serializers.ModelSerializer):
    payments = PaymentsSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'created_at', 'updated_at', 'amount', 'required_date', 'is_now',
                  'status', 'client', 'created_by', 'customer', 'division', 'updated_by', 'payments']

    def create(self, validated_data):
        payments_data = validated_data.pop('payments')
        order = Order.objects.create(**validated_data)
        for payment in payments_data:
            payment = dict(payment)
            payment = Payment.objects.create(**payment)
            payment.payments.add(order)
        return order
