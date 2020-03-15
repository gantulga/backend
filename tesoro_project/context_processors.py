from django.conf import settings
from structure_app.models import Configuration_value
from django.template import Context

def configration_values(request):
	configs = Configuration_value.objects.get(pk=1)
	return {'configration_values': configs}