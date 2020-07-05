from django.contrib import admin
from .models import *

admin.site.site_header = 'Tesoro Center - Хэрэглэгчийн програм'


class WalletAdmin(admin.ModelAdmin):
    list_display = ('get_wallet_owner', 'account')

    def get_wallet_owner(self, obj):
        return obj.owner.first_name


class MoneyTransferTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


# Register your models here.
admin.site.register(Investment)
admin.site.register(Loan)
admin.site.register(Currency)
admin.site.register(Money_transfer_type, MoneyTransferTypeAdmin)
admin.site.register(Wallet, WalletAdmin)
admin.site.register(Budget_type)
admin.site.register(Budget)
admin.site.register(Money_transfer)
