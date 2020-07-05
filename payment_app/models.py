from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.validators import MaxValueValidator, MinValueValidator
#from structure_app.models import Division, Client, Customer
#from product_app.models import Product


User = get_user_model()
# Create your models here.


class Createdinfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by = models.ForeignKey(
        User, related_name='%(class)s_createdby', null=True, blank=True, on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True


class Modifiedinfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(
        User, related_name='%(class)s_createdby', null=True, blank=True, on_delete=models.DO_NOTHING)
    updated_by = models.ForeignKey(
        User, related_name='%(class)s_modifiedby', null=True, blank=True, on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True

# Захиалга


class Order(Modifiedinfo):
    client = models.ForeignKey('structure_app.Client', null=False,
                               blank=False, on_delete=models.DO_NOTHING, related_name="orders")
    customer = models.ForeignKey('structure_app.Customer', null=True,
                                 blank=True, on_delete=models.DO_NOTHING, related_name="orders")
    amount = models.DecimalField(
        max_digits=14, decimal_places=2, null=True, blank=True)
    required_date = models.DateTimeField(null=False, blank=False)
    is_now = models.BooleanField(default=1)
    status = models.CharField(null=False, max_length=255)
    division = models.ForeignKey('structure_app.Division', null=False,
                                 blank=False, on_delete=models.DO_NOTHING, related_name="orders")
    products = models.ManyToManyField(
        'product_app.Product', through='Order_detial', related_name="products")
    payments = models.ManyToManyField(
        'Payment', through='Order_payments', related_name="payments")
    shift_work = models.ForeignKey('structure_app.Shift_work', related_name='orders',
                                   null=True, blank=True, on_delete=models.DO_NOTHING)

# Захиалга дотрох бүтээгдэхүүнүүд


class Order_detial(Modifiedinfo):
    order = models.ForeignKey(
        'Order', on_delete=models.DO_NOTHING, related_name="order_detials")
    product = models.ForeignKey(
        'product_app.Product', on_delete=models.DO_NOTHING, related_name="order_detials")
    client = models.ForeignKey('structure_app.Client', on_delete=models.DO_NOTHING,
                               related_name="client_detials", null=True, blank=True)
    quantity = models.PositiveIntegerField(null=False, default=1)
    discount = models.PositiveIntegerField(null=False, default=0)
    fr_date = models.DateTimeField(null=True, blank=True)
    to_date = models.DateTimeField(null=True, blank=True)
    discount_rate = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    subtotal = models.DecimalField(
        max_digits=14, decimal_places=2, null=False, blank=False)
    is_deleted = models.BooleanField(default=0)
    why_deleted = models.TextField(null=True, blank=True)
    deleted_date = models.DateTimeField(null=True, blank=True)
    fr_client = models.ForeignKey('structure_app.Client', on_delete=models.DO_NOTHING,
                                  related_name="sent_order_detials", null=True, blank=True)
    shift_work = models.ForeignKey('structure_app.Shift_work', related_name='order_detials',
                                   null=True, blank=True, on_delete=models.DO_NOTHING)

# Захиалгын тооцоонууд


class Order_payments(Modifiedinfo):
    order = models.ForeignKey(
        'Order', on_delete=models.DO_NOTHING)
    payment = models.ForeignKey(
        'Payment', on_delete=models.DO_NOTHING)

# Захиалгын төлбөр


class Bill(Modifiedinfo):
    client = models.ForeignKey('structure_app.Client', null=False, blank=False,
                               on_delete=models.DO_NOTHING, related_name="client_bills")
    total_amount = models.DecimalField(
        max_digits=14, decimal_places=2, null=False, blank=False, default=0)
    discount_rate = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    discounted_amount = models.DecimalField(
        max_digits=14, decimal_places=2, null=False, blank=False, default=0)
    amount = models.DecimalField(
        max_digits=14, decimal_places=2, null=False, blank=False, default=0)
    status = models.CharField(null=False, max_length=255)
    got_ebarimt = models.BooleanField(default=0)
    did_splited = models.BooleanField(default=0)
    company_name = models.CharField(null=False, max_length=255)
    company_register = models.CharField(null=False, max_length=255)
    division = models.ForeignKey('structure_app.Division', null=False,
                                 blank=False, on_delete=models.DO_NOTHING, related_name="division_bills")
    customer = models.ForeignKey('structure_app.Customer', null=False,
                                 blank=False, on_delete=models.DO_NOTHING, related_name="customer_bills")

# Төлбөрийн төлөлт


class Payment(Modifiedinfo):
    confirmed_by = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.DO_NOTHING, related_name="payments")
    amount = models.DecimalField(
        max_digits=14, decimal_places=2, null=True, blank=True)
    wallet = models.ForeignKey('financial_app.Wallet', null=False, blank=False,
                               on_delete=models.DO_NOTHING, default=999, related_name="payments")
    bills = models.ManyToManyField('Bill', through='Payment_bills')
    shift_work = models.ForeignKey('structure_app.Shift_work', related_name='payments',
                                   null=True, blank=True, on_delete=models.DO_NOTHING)
    division = models.ForeignKey('structure_app.Division', null=True, blank=True,
                                 on_delete=models.DO_NOTHING, related_name="payments")


# Тооцооны баримтууд


class Payment_bills(Modifiedinfo):
    bill = models.ForeignKey(
        'Bill', on_delete=models.DO_NOTHING, related_name="bill_payments")
    payment = models.ForeignKey(
        'Payment', on_delete=models.DO_NOTHING, related_name="payment_bills")

# POS машины нэгтгэл


class Pos_account_consolidation(Modifiedinfo):
    shift_work = models.ForeignKey('structure_app.Shift_work', related_name='pos_account_consolidation',
                                   null=True, blank=True, on_delete=models.DO_NOTHING)
    division = models.ForeignKey('structure_app.Division', null=False, blank=False,
                                 on_delete=models.DO_NOTHING, related_name="Pos_account_consolidations")
    fr_date = models.DateTimeField(null=False, blank=False)
    to_date = models.DateTimeField(null=False, blank=False)
    account = models.ForeignKey('financial_app.Wallet', null=False, blank=False,
                                on_delete=models.DO_NOTHING, related_name="Pos_account_consolidations")
    amount = models.DecimalField(
        max_digits=14, decimal_places=2, null=True, blank=True)
    person_of_charge = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.DO_NOTHING, related_name="person_of_charge_pos")
    confirmed_by = models.ForeignKey(
        User, null=False, blank=False, on_delete=models.DO_NOTHING, related_name="confirmed_by_pos")
