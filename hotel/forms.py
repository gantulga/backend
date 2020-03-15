from django import forms
from functools import partial
from structure_app.models import Division, Client, Customer
from product_app.models import Product
from .models import Hotel_client_log

DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class CheckInRoomForm(forms.Form):
	cost = forms.DecimalField(max_digits=8, decimal_places=0)
	is_now = forms.BooleanField()
	fr_date =  forms.DateTimeField(
        #input_formats=['%d/%m/%Y %H:%M'],
        #widget=forms.DateTimeInput(attrs={
        #    'class': 'form-control datetimepicker-input',
        #    'data-target': '#fr_date'
        #})
    )
	to_date =  forms.DateTimeField(
        #input_formats=['%d/%m/%Y %H:%M'],
        #widget=forms.DateTimeInput(attrs={
        #    'class': 'form-control datetimepicker-input',
        #    'data-target': '#to_date'
        #})
    )
	quantity = forms.IntegerField()