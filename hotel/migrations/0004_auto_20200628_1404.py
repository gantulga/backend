# Generated by Django 3.0.2 on 2020-06-28 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_auto_20200628_1400'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel_client_log',
            old_name='choices_type',
            new_name='choices',
        ),
    ]
