# Generated by Django 3.0.2 on 2020-03-15 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('structure_app', '0012_configuration_value_hotel_must_leave_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration_value',
            name='hotel_start_time_of_timeService',
            field=models.CharField(max_length=2, null=True),
        ),
    ]