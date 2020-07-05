from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from flask import request
from django.db.models.signals import post_save, pre_save
from notification.signals import create_welcome_message


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

# Газар нэгж


class Division(Createdinfo):
    name = models.CharField(null=False, max_length=255)
    description = models.TextField(null=False)
    users = models.ManyToManyField(
        User, db_table="auth_user_divisions", related_name='divisions')

    def __str__(self):
        return self.name

# Үйлчилүүлэгч (Division нь hotel бйавал client нь өрөөний дугаар байх болно.)


class Client(Createdinfo):
    division = models.ForeignKey(
        'Division', null=False, blank=False, on_delete=models.PROTECT, related_name="clients")
    number = models.IntegerField(null=False)
    description = models.TextField(null=False, max_length=255)
    free = models.BooleanField(default=1)
    clean = models.BooleanField(default=1)
    minibarFull = models.BooleanField(default=1)

    class Meta:
        unique_together = ('division', 'number')

    def __str__(self):
        # return str(self.number)
        return u"%s - %s" % (self.division, self.number)

#post_save.connect(create_welcome_message, sender=Client)


# Бүртгэлтэй үйлчилүүлэгчийн мэдээлэл, байнга үйлчилүүлж манайд өөрөө бүртгүүлсэн хүмүүс
class Customer(Createdinfo):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    lastname = models.CharField(null=True, max_length=255)
    firstname = models.CharField(null=False, max_length=255)
    register = models.CharField(null=False, max_length=255, unique=True)
    address = models.CharField(null=True, max_length=255, default='')
    address2 = models.CharField(null=True, max_length=255, default='')
    workname = models.CharField(null=True, max_length=255, default='')
    workaddress = models.CharField(null=True, max_length=255, default='')
    mobile = models.IntegerField(blank=True, null=True, default=0)
    phone = models.IntegerField(blank=True, null=True, default=0)
    email = models.EmailField(blank=True, null=True, default=0)
    discount_rate = models.IntegerField(default=0, validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    information = models.TextField(null=True, default='')

    # class Meta:
    #     unique_together = ('register', 'mobile')

    def __str__(self):
        return self.lastname


# Бүртгэлтэй үйлчилүүлэгчийн мэдээлэл, байнга үйлчилүүлж манайд өөрөө бүртгүүлсэн хүмүүс
class User_Profile(Modifiedinfo):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=False, blank=False)
    lastname = models.CharField(null=False, max_length=255)
    firstname = models.CharField(null=False, max_length=255)
    register = models.CharField(null=False, max_length=255)
    address = models.CharField(null=False, max_length=255)
    address2 = models.CharField(null=True, max_length=255)
    mobile = models.IntegerField(blank=False, null=False)
    phone = models.IntegerField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    information = models.TextField(null=True)

    who_are = models.CharField(blank=True, null=True, max_length=10)
    near_people_name = models.CharField(blank=True, null=True, max_length=30)
    near_people_mobile = models.IntegerField(blank=True, null=True)
    near_people_address = models.CharField(
        blank=True, null=True, max_length=255)

    school1 = models.CharField(blank=False, null=False, max_length=100)
    school2 = models.CharField(blank=False, null=False, max_length=100)
    school3 = models.CharField(blank=False, null=False, max_length=100)

    citizen_identity_card_copy = models.BooleanField(default=0)
    white_card_of_hospital = models.BooleanField(default=0)
    number_of_white_card = models.CharField(null=True, max_length=30)
    social_security_book = models.BooleanField(default=0)
    number_of_social_security_book = models.CharField(null=True, max_length=30)
    health_book = models.BooleanField(default=0)
    number_of_health_book = models.CharField(null=True, max_length=30)

    first_contract = models.BooleanField(default=0)
    number_of_first_contract = models.CharField(null=True, max_length=30)
    second_contract = models.BooleanField(default=0)
    number_of_second_contract = models.CharField(null=True, max_length=30)
    first_salary = models.BigIntegerField(blank=True, null=True)
    second_salary = models.BigIntegerField(blank=True, null=True)

    bank_name = models.CharField(null=True, max_length=30)
    account_of_bank = models.BigIntegerField(blank=True, null=True)

    avatar = models.ImageField(
        upload_to='user_avatars/%Y%m%d%H%H%S', blank=True, null=True)

    class Meta:
        unique_together = ('register', 'mobile')

    def __str__(self):
        return self.name

# Бүртгэлтэй үйлчилүүлэгчийн мэдээлэл, байнга үйлчилүүлж манайд өөрөө бүртгүүлсэн хүмүүс


class Configuration_value(models.Model):
    program_name = models.CharField(null=True, max_length=255)
    program_description = models.TextField(null=True, max_length=255)
    program_favicon_url = models.CharField(null=True, max_length=255)
    program_logo_url = models.CharField(null=True, max_length=255)
    noat_tax = models.IntegerField(default=0, validators=[MinValueValidator(
        0), MaxValueValidator(100)], blank=True, null=True)
    capital_city_tax = models.IntegerField(default=0, validators=[
                                           MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    hotel_deadline_time_of_dayService = models.CharField(
        null=True, max_length=2)
    hotel_start_time_of_timeService = models.CharField(
        null=True, max_length=2)
    hotel_deadline_time_of_timeService = models.CharField(
        null=True, max_length=2)
    hotel_minimum_time_of_timeService = models.CharField(
        null=True, max_length=2)
    hotel_must_leave_time = models.CharField(
        null=True, max_length=2)


class Shift_work(Createdinfo):
    division = models.ForeignKey(
        'Division', null=False, blank=False, on_delete=models.PROTECT, related_name="Shift_works")
    worker = models.ForeignKey(User, related_name='shift_works',
                               null=True, blank=True, on_delete=models.DO_NOTHING)
    worker_confirm = models.BooleanField(default=0)
    controller = models.ForeignKey(User, related_name='controller_shift_works',
                                   null=True, blank=True, on_delete=models.DO_NOTHING)
    controller_confirm = models.BooleanField(default=0)
    finished = models.BooleanField(default=0)
