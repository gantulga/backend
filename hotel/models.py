from django.db import models

# Create your models here.
ROW_TYPE_CHOICES = (
    ('1', 'Өрөөний мэдээлэл'),
    ('2', 'Зочины тоон мэдээлэл'),
    ('3', 'Цэвэрлэгээний мэдээлэл'),
    ('4', 'Мини барны мэдээлэл'),
)

# ROOM_INFO_CHOICES = (
#     ('0', '---'),
#     ('in', 'Зочинтой'),
#     ('out', 'Сул'),
# )

# LOGIN_INFO_CHOICES = (
#     ('0', '---'),
#     ('in', 'Зочин орсон'),
#     ('out', 'Зочин гарсан'),
# )

# CLEANING_INFO_CHOICES = (
#     ('0', '---'),
#     ('c_s', 'Цэвэрлэж эхэлсэн'),
#     ('c_e', 'Цэвэрлэж дууссан'),
# )

# BAR_REFILLED_INFO_CHOICES = (
#     ('0', '---'),
#     ('b_r', 'Мини бар цэнэглэгдсэн'),
#     ('b_u', 'Мини бар цэнэглэгдээгүй'),
# )

# Client-ийн орсон гарсан, цэвэрлэсэн, мини бар дүүргэлтийн мэдээлэл (Division нь hotel бйавал өрөөнд хүн орсон гарсан огноог бүртгэнэ.)


class Hotel_client_log(models.Model):
    client = models.ForeignKey('structure_app.Client', null=True,
                               blank=True, on_delete=models.DO_NOTHING, related_name='logs')

    choices_type = models.CharField(
        max_length=3, choices=ROW_TYPE_CHOICES, null=False)
    value = models.CharField(max_length=3, null=False)
    number = models.IntegerField(null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False)

    def __str__(self):
        return str(self.choices_type)

# Зочид буудлын мини барнд байгаа эд зүйлсийн байх ёстой тооны мэдээллийг агуулна.


class Hotel_client_item(models.Model):
    client = models.ForeignKey('structure_app.Client', null=False, blank=False,
                               on_delete=models.DO_NOTHING, related_name='client_items')
    product = models.ForeignKey('product_app.Product', null=False, blank=False,
                                on_delete=models.DO_NOTHING, related_name='client_items')
    quantity = models.IntegerField(blank=False, null=False, default=0)


class Hotel_client_item_eelj(models.Model):
    client = models.ForeignKey('structure_app.Client', null=False, blank=False,
                               on_delete=models.DO_NOTHING, related_name='client_items_eelj')
    product = models.ForeignKey('product_app.Product', null=False, blank=False,
                                on_delete=models.DO_NOTHING, related_name='client_items_eelj')
    quantity = models.IntegerField(blank=False, null=False, default=0)
