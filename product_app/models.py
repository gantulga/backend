from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
#from structure_app.models import Division
#from financial_app.models import Budget
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.contrib.contenttypes.fields import GenericRelation
import sys

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

# Бүтээгдэхүүний ангилал


class Product_category(Createdinfo):
    parent = models.ForeignKey('self', null=True, blank=True,
                               on_delete=models.PROTECT, related_name="child_categories")
    name = models.CharField(null=False, max_length=255)
    description = models.TextField(null=False, max_length=255)

    def __str__(self):
        return self.name

# Түүхий эдийн ангилал


class Commodity_category(Createdinfo):
    parent = models.ForeignKey('self', null=True, blank=True,
                               on_delete=models.PROTECT, related_name="child_categories")
    name = models.CharField(null=False, max_length=255)
    description = models.TextField(null=False, max_length=255)
    Division = models.ManyToManyField(
        'structure_app.Division', db_table="product_app_division_commodity_categories")

    def __str__(self):
        return self.name

# Түүхий эд


class Commodity(Createdinfo):
    name = models.CharField(null=False, max_length=255)
    description = models.TextField(null=True, max_length=255)
    size_type = models.ForeignKey(
        'Size_type', on_delete=models.DO_NOTHING, null=True, related_name="commodities")
    unit_size = models.PositiveIntegerField(null=True, blank=True)
    categories = models.ManyToManyField(
        'Commodity_category', db_table="product_app_commodity_categories", related_name="commodities")

    def __str__(self):
        return self.name

# Бүтээгдэхүүн эд


class Product(Createdinfo):
    name = models.CharField(null=False, max_length=255)
    description = models.TextField(null=True, max_length=255)
    cost = models.DecimalField(max_digits=14, decimal_places=2)
    categories = models.ManyToManyField(
        'Product_category', db_table="product_app_product_categories", related_name="products")
    commodities = models.ManyToManyField('Commodity', through='Ingredient')
    client = models.ForeignKey('structure_app.Client', related_name='client_products',
                               on_delete=models.DO_NOTHING, null=True, blank=True)
    division = models.ForeignKey('structure_app.Division', related_name='division_products',
                                 on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return self.id

    # def __unicode__(self):
    #     return self.id

# Хэмжих нэгжийн төрлүүд, ш, ш-гр, грамм


class Size_type(Createdinfo):
    name = models.CharField(null=False, max_length=30)
    abbreviation = models.CharField(null=False, max_length=10)
    description = models.TextField(null=False, max_length=255)

    def __str__(self):
        return self.abbreviation

# Бүтээгдэхүүнд орох түүхий эдийн орц болон хэмжээ


class Ingredient(Createdinfo):
    commodity = models.ForeignKey(
        'Commodity', on_delete=models.CASCADE, related_name="ingredients")
    product = models.ForeignKey(
        'Product', on_delete=models.CASCADE, related_name="ingredients")
    size = models.PositiveIntegerField(null=False)
    size_type = models.ForeignKey(
        'Size_type', on_delete=models.DO_NOTHING, null=False, related_name="ingredients")

    class Meta:
        unique_together = ('commodity', 'product')

    def __str__(self):
        return '{} ---> {} : size = {}'.format(self.commodity.name, self.product.name, self.size)

# Түүхий эдийг бүтээгдэхүүнд орж байна уу аль эсвэл ажилчид хоорондоо шилжүүлсэн үү гэдгийг харуулах ангилал


class Item_transfer_type(Createdinfo):
    name = models.CharField(null=False, max_length=30)
    description = models.TextField(null=True, max_length=255)

    def __str__(self):
        return self.name

# Бараа татах үед аль дэлгүүрээс авсанаа энд бүртгэж байх юм.


class Store(Createdinfo):
    name = models.CharField(null=False, max_length=30)
    description = models.TextField(null=True, max_length=255)

# Түүхий эд нэмэгдэх, бүтээгдэхүүнд ороод хасагдах, ажилчидад олгох, шилжүүлэх бүх гүйлгээний мэдээлэл


class Item_transfer(Modifiedinfo):
    item_transfer_type = models.ForeignKey(
        'Item_transfer_type', related_name='item_transfers', on_delete=models.PROTECT, null=False)
    commodity = models.ForeignKey(
        'Commodity', on_delete=models.DO_NOTHING, null=True, blank=True, related_name="transfers")
    product = models.ForeignKey(
        'Product', on_delete=models.DO_NOTHING, null=True, blank=True, related_name="transfers")
    # Хоолны болон Коктейлийн орцонд орох
    to_product = models.ForeignKey('Product', on_delete=models.DO_NOTHING,
                                   null=True, blank=True, related_name="ingredients_transfer")
    product_quantity = models.PositiveIntegerField(null=True, blank=True)
    # Худалдагдах
    order_detial = models.ForeignKey(
        'payment_app.Order_detial', related_name='item_transfers', null=True, blank=True, on_delete=models.DO_NOTHING)
    fr_division = models.ForeignKey(
        'structure_app.Division', related_name='sending_item_transfers', null=True, blank=True, on_delete=models.DO_NOTHING)
    to_division = models.ForeignKey('structure_app.Division', related_name='coming_item_transfers',
                                    null=False, blank=False, on_delete=models.DO_NOTHING)
    fr_client = models.ForeignKey('structure_app.Client', related_name='sending_item_transfers',
                                  null=True, blank=True, on_delete=models.DO_NOTHING)
    to_client = models.ForeignKey('structure_app.Client', related_name='coming_item_transfers',
                                  null=False, blank=False, on_delete=models.DO_NOTHING)
    fr_user = models.ForeignKey(User, related_name='sending_item_transfers',
                                null=False, blank=False, on_delete=models.DO_NOTHING)
    to_user = models.ForeignKey(User, related_name='coming_item_transfers',
                                null=False, blank=False, on_delete=models.DO_NOTHING)
    # Энэ шилжүүлгийг хянасан эсэх? мөн хэн хянасан
    is_confirmed = models.BooleanField(default=0)
    confirmed_by = models.ForeignKey(
        User, related_name='item_transfer_confirmed_by', null=True, blank=True, on_delete=models.DO_NOTHING)
    # Худалдан авч буй тохиолдолд доорх утгыг бөглөнө
    store = models.ForeignKey('Store', null=True, blank=True,
                              on_delete=models.PROTECT, related_name="bought_item_transfers")
    recieved_ebarimt = models.BooleanField(default=0)
    comment = models.TextField(null=True, blank=True)
    budget = models.ForeignKey('financial_app.Budget', null=True, blank=True,
                               on_delete=models.DO_NOTHING, related_name="bought_item_transfers")
    unit_size = models.PositiveIntegerField(null=True, blank=True)
    unit_price = models.DecimalField(
        max_digits=14, decimal_places=2, null=True, blank=True)
    total_amount = models.DecimalField(
        max_digits=14, decimal_places=2, null=True, blank=True)
    # Шилжүүлж буй түүхий эдийн хэмжээ
    quantity = models.PositiveIntegerField(null=True, blank=True)
    size = models.PositiveIntegerField(null=True, blank=True)

# Түүхий эдийн үлдэгдэл Clien болон ажилтанд ямар байгааг бүртгэх Balance table


class Commodity_balance(Modifiedinfo):
    division = models.ForeignKey('structure_app.Division', related_name='commodity_balances',
                                 null=True, blank=True, on_delete=models.DO_NOTHING)
    client = models.ForeignKey('structure_app.Client', related_name='commodity_balances',
                               null=True, blank=True, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, related_name='commodity_balances',
                             null=True, blank=True, on_delete=models.DO_NOTHING)
    commodity = models.ForeignKey(
        'Commodity', on_delete=models.DO_NOTHING, null=False, related_name="commodity_balances")
    # Түүхий эдийн хэмжээ
    quantity = models.PositiveIntegerField(null=False, blank=False)
    size = models.PositiveIntegerField(null=False, blank=False)


# Барилгын үндсэн хөрөнгийн жагсаалт байх юм.
class Basic_asset(Modifiedinfo):
    division = models.ForeignKey('structure_app.Division', related_name='basic_assets',
                                 null=True, blank=True, on_delete=models.DO_NOTHING)
    name = models.CharField(null=False, max_length=30)
    description = models.TextField(null=True, max_length=255)
    real_price = models.DecimalField(max_digits=14, decimal_places=2)
    rised_price = models.DecimalField(max_digits=14, decimal_places=2)
    code = models.CharField(null=False, max_length=30)
    photo = models.ImageField(upload_to='asset_images')

    def __str__(self):
        return self.name
        # return '{} - {}'.format(self.division.name, self.name)

# Барилгын үндсэн хөрөнгийн тооллогын талбар байх юм.


class Basic_asset_count(Modifiedinfo):
    basic_asset = models.ForeignKey(
        Basic_asset, related_name='counts', null=False, blank=False, on_delete=models.DO_NOTHING)
    counted_day = models.DateField(null=False)
    prev_quantity = models.PositiveIntegerField(null=False)
    quantity_balance = models.PositiveIntegerField(null=False)
    quantity_increased = models.PositiveIntegerField(null=False)
    quantity_deducted = models.PositiveIntegerField(null=False)
    information = models.TextField(null=True)
    counted_by = models.ForeignKey(
        User, related_name='counted_by', null=False, blank=False, on_delete=models.DO_NOTHING)
    controlled_by = models.ForeignKey(
        User, related_name='controlled_by', null=True, blank=True, on_delete=models.DO_NOTHING)
    controll_confirmed = models.BooleanField(default=0)

# Барилгын эд зүйлсийн эвдрэлийн бүртгэл.


class broken_item (Modifiedinfo):
    basic_asset = models.ForeignKey(
        'Basic_asset', related_name='broken_basic_assets', null=False, blank=False, on_delete=models.DO_NOTHING)
    product = models.ForeignKey('Product', related_name='broken_products',
                                null=False, blank=False, on_delete=models.DO_NOTHING)
    commodity = models.ForeignKey('Commodity', related_name='broken_commodities',
                                  null=False, blank=False, on_delete=models.DO_NOTHING)
    size = models.PositiveIntegerField(null=False)
    size_type = models.ForeignKey(
        'Size_type', on_delete=models.DO_NOTHING, null=True, related_name="broken_items")
    description = models.TextField(null=True, max_length=255)
    damage_paid = models.BooleanField(default=0)
    money_transfer = models.ForeignKey(
        'financial_app.Money_transfer', related_name='broken_items_money', null=False, blank=False, on_delete=models.DO_NOTHING)
    money_transfer_status = models.CharField(
        null=False, default='тодорхойгүй', max_length=30)
