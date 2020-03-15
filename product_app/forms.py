from django import forms
from .models import Item_transfer

class InsertItemForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(InsertItemForm, self).__init__(*args, **kwargs)
		#self.fields['quantity'].widget.attrs = {'class':'form-control'}
		for name, field in self.fields.items():
			field.widget.attrs.update({'class':'form-control', 'id':name})
			field.label = ''

	class Meta:
		model = Item_transfer
		fields = [
			'commodity',
			'product',
			'to_division',
			'to_client',
			'to_user',
			'is_confirmed',
			'confirmed_by',
			'store',
			'recieved_ebarimt',
			'comment',
			'budget',
			'unit_size',
			'unit_price',
			'total_amount',
			'quantity',
			'size',
		]