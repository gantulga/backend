# Generated by Django 3.0.2 on 2020-03-16 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure_app', '0016_auto_20200316_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mobile',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]