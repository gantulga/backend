from django.contrib import admin
from .models import *

admin.site.site_header = 'Tesoro Center - Хэрэглэгчийн програм'

class Basis_assetAdmin(admin.ModelAdmin):
	list_display = ('name', 'division')
	exclude = ['created_by', 'updated_by']

	def save_model(self, request, obj, form, change):
		if not change:
			obj.created_by = request.user
		elif change:
			obj.updated_by = request.user
		obj.save()

class Basis_asset_countAdmin(admin.ModelAdmin):
	list_display = ('basic_asset', 'quantity_balance', 'counted_day')

class ProductCategoryAdmin(admin.ModelAdmin):
	list_display = ('parent', 'name', 'description')

class ProductAdmin(admin.ModelAdmin):
	#list_display = ('parent', 'name', 'description')
	exclude = ['created_by']


# Register your models here.
admin.site.register(Product_category, ProductCategoryAdmin)
admin.site.register(Commodity_category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Commodity)
admin.site.register(Size_type)
admin.site.register(Ingredient)
admin.site.register(Item_transfer_type)
admin.site.register(Store)
admin.site.register(Item_transfer)
admin.site.register(Basic_asset, Basis_assetAdmin)
admin.site.register(Basic_asset_count, Basis_asset_countAdmin)
admin.site.register(broken_item)