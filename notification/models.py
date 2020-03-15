from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Notification(models.Model):
	title = models.CharField(max_length=256)
	message = models.TextField(null=False, blank=False)
	viewed = models.BooleanField(default=False)
	user = models.ForeignKey(User, null=False, blank=False, on_delete=models.DO_NOTHING)
	url = models.TextField(null=True, blank=True)