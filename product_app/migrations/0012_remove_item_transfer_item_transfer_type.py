# Generated by Django 3.0.2 on 2020-02-19 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0011_item_transfer_item_transfer_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item_transfer',
            name='Item_transfer_type',
        ),
    ]