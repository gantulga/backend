# Generated by Django 3.0.2 on 2020-02-16 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financial_app', '0002_auto_20200211_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=14, null=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='balance',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=14, null=True),
        ),
        migrations.AlterField(
            model_name='currency',
            name='ratio',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
        migrations.AlterField(
            model_name='investment',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
        migrations.AlterField(
            model_name='investment',
            name='issued_money',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
        migrations.AlterField(
            model_name='investment',
            name='refunded_money',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=14),
        ),
        migrations.AlterField(
            model_name='loan',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
        migrations.AlterField(
            model_name='loan',
            name='issued_money',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
        migrations.AlterField(
            model_name='loan',
            name='refunded_money',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=14),
        ),
        migrations.AlterField(
            model_name='money_transfer',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=14, null=True),
        ),
        migrations.AlterField(
            model_name='money_transfer',
            name='msg_info_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=14, null=True),
        ),
        migrations.AlterField(
            model_name='money_transfer',
            name='transfer_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=14, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='bank_transfer_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=14, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='msg_info_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=14, null=True),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='transfer_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=14, null=True),
        ),
    ]