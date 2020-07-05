from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
#from structure_app.models import Division, Client, Customer
#from payment_app.models import Bill, Payment


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

# Хөрөнгө оруулалт


class Investment(Createdinfo):
    investor = models.CharField(null=False, max_length=255)
    issued_money = models.DecimalField(
        max_digits=14, decimal_places=2, null=False, blank=False)
    refunded_money = models.DecimalField(
        max_digits=14, decimal_places=2, null=False, blank=False, default=0)
    balance = models.DecimalField(
        max_digits=14, decimal_places=2, null=False, blank=False)
    issued_date = models.DateTimeField(null=True, blank=True)
    refunded_date = models.DateTimeField(null=True, blank=True)
    will_refund = models.BooleanField(default=0)

    def __unicode__(self):
        return self.investor

    def __str__(self):
        return self.investor

# Зээл


class Loan(Createdinfo):
    lender = models.CharField(null=False, max_length=255)
    issued_money = models.DecimalField(
        max_digits=14, decimal_places=2, null=False, blank=False)
    refunded_money = models.DecimalField(
        max_digits=14, decimal_places=2, null=False, blank=False, default=0)
    balance = models.DecimalField(
        max_digits=14, decimal_places=2, null=False, blank=False)
    loan_rate = models.IntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    issued_date = models.DateTimeField(null=True, blank=True)
    refunded_date = models.DateTimeField(null=True, blank=True)

# Вальют


class Currency(Createdinfo):
    name = models.CharField(null=False, max_length=255)
    ratio = models.DecimalField(
        max_digits=14, decimal_places=2, null=False, blank=False)
    country = models.CharField(null=True, max_length=255)

# Мөнгөн шилжүүлгийн төрөл


class Money_transfer_type(Createdinfo):
    name = models.CharField(null=False, max_length=255)
    description = models.TextField(null=True)

#Данс, түрийвч


class Wallet(Createdinfo):
    name = models.CharField(null=False, max_length=255)
    description = models.TextField(null=True)
    bank = models.CharField(null=True, max_length=255)
    account = models.BigIntegerField(null=True)
    balance = models.DecimalField(
        max_digits=14, decimal_places=2, null=False, blank=False, default=0)
    owner = models.ForeignKey(User, related_name='wallets',
                              null=True, blank=True, on_delete=models.DO_NOTHING)
    msg_info_fee = models.DecimalField(
        max_digits=14, decimal_places=2, null=True, blank=True, default=0)
    transfer_fee = models.DecimalField(
        max_digits=14, decimal_places=2, null=True, blank=True, default=0)
    bank_transfer_fee = models.DecimalField(
        max_digits=14, decimal_places=2, null=True, blank=True, default=0)
    division = models.ForeignKey('structure_app.Division', related_name='wallets',
                                 null=True, blank=True, on_delete=models.DO_NOTHING)

# Төсвийн ангилал


class Budget_type(Createdinfo):
    name = models.CharField(null=False, max_length=255)
    description = models.TextField(null=True)

# Төсөв


class Budget(Modifiedinfo):
    name = models.CharField(null=False, max_length=255)
    budget_type = models.ForeignKey(
        'Budget_type', related_name='%(class)s_type', null=False, blank=False, on_delete=models.DO_NOTHING)
    coordinator = models.ForeignKey(
        User, related_name='%(class)s_coordinator', null=True, blank=True, on_delete=models.DO_NOTHING)
    description = models.TextField(null=True)
    amount = models.DecimalField(
        max_digits=14, decimal_places=2, null=True, blank=True, default=0)
    balance = models.DecimalField(
        max_digits=14, decimal_places=2, null=True, blank=True, default=0)
    status = models.CharField(null=False, max_length=255, default='Төсөвлөсөн')

# Мөнгөн шилжүүлгийн өгөгдөл


class Money_transfer(Modifiedinfo):
    fr_wallet = models.ForeignKey(
        'Wallet', related_name='fr_wallet', null=True, blank=True, on_delete=models.DO_NOTHING)
    to_wallet = models.ForeignKey(
        'Wallet', related_name='to_wallet', null=True, blank=True, on_delete=models.DO_NOTHING)
    msg_info_fee = models.DecimalField(
        max_digits=14, decimal_places=2, null=True, blank=True, default=0)
    transfer_fee = models.DecimalField(
        max_digits=14, decimal_places=2, null=True, blank=True, default=0)
    payment = models.ForeignKey(
        'payment_app.Payment', null=True, blank=True, on_delete=models.DO_NOTHING)
    bill = models.ForeignKey(
        'payment_app.Bill', null=True, blank=True, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(
        'structure_app.Customer', null=True, blank=True, on_delete=models.DO_NOTHING)
    division = models.ForeignKey(
        'structure_app.Division', null=True, blank=True, on_delete=models.DO_NOTHING)
    description = models.TextField(null=True)
    money_transfer_type = models.ForeignKey(
        'Money_transfer_type', null=False, blank=False, on_delete=models.DO_NOTHING)
    fr_user = models.ForeignKey(User, related_name='moneytransfer_fr_user',
                                null=True, blank=True, on_delete=models.DO_NOTHING)
    to_user = models.ForeignKey(User, related_name='moneytransfer_to_user',
                                null=True, blank=True, on_delete=models.DO_NOTHING)
    fr_budget = models.ForeignKey(
        'Budget', related_name='fr_budget', null=True, blank=True, on_delete=models.DO_NOTHING)
    to_budget = models.ForeignKey(
        'Budget', related_name='to_budget', null=True, blank=True, on_delete=models.DO_NOTHING)
    wanna_delete = models.BooleanField(default=0)
    currency = models.ForeignKey(
        'Currency', null=False, blank=False, on_delete=models.DO_NOTHING, default=1)
    recieved_ebarimt = models.BooleanField(default=0)
    fr_investment = models.ForeignKey(
        'Investment', related_name='fr_investment', null=True, blank=True, on_delete=models.DO_NOTHING)
    to_investment = models.ForeignKey(
        'Investment', related_name='to_investment', null=True, blank=True, on_delete=models.DO_NOTHING)
    fr_loan = models.ForeignKey(
        'Loan', related_name='fr_loan', null=True, blank=True, on_delete=models.DO_NOTHING)
    to_loan = models.ForeignKey(
        'Loan', related_name='to_loan', null=True, blank=True, on_delete=models.DO_NOTHING)
    amount = models.DecimalField(
        max_digits=14, decimal_places=2, null=True, blank=True, default=0)
