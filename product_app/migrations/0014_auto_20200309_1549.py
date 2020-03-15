# Generated by Django 3.0.2 on 2020-03-09 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0013_item_transfer_item_transfer_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='categories',
            field=models.ManyToManyField(db_table='product_app_commodity_categories', related_name='commodities', to='product_app.Commodity_category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(db_table='product_app_product_categories', related_name='products', to='product_app.Product_category'),
        ),
    ]