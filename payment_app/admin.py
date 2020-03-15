from django.contrib import admin
from .models import *

admin.site.site_header = 'Tesoro Center - Хэрэглэгчийн програм'

class OrderAdmin(admin.ModelAdmin):
	#list_display = ('name', 'division')
	exclude = ['created_by', 'updated_by']

	def save_model(self, request, obj, form, change):
		if not change:
			obj.created_by = request.user
		elif change:
			obj.updated_by = request.user
		obj.save()

# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(Order_detial)
admin.site.register(Bill)
admin.site.register(Payment)