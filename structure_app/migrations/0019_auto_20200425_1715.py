# Generated by Django 3.0.2 on 2020-04-25 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure_app', '0018_auto_20200323_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='clean',
            field=models.BooleanField(default=1),
        ),
        migrations.AddField(
            model_name='client',
            name='free',
            field=models.BooleanField(default=1),
        ),
        migrations.AddField(
            model_name='client',
            name='minibarFull',
            field=models.BooleanField(default=1),
        ),
    ]