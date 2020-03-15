from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from notification.models import Notification
from flask import request

def create_welcome_message(sender, instance, **kwargs):
	print(sender)
	print(instance)
	print(kwargs)
	if kwargs.get('created') == True:
		message = str(instance)+"client added!"
		user = User.objects.get(id=instance.created_by.id)
		print(user)
		notify = Notification.objects.create(title="client added",
												message=message,
												viewed=False,
												url="/",
												user=user)