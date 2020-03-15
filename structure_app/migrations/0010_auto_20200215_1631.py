# Generated by Django 3.0.2 on 2020-02-15 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure_app', '0009_delete_hotel_client_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='division',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='clients', to='structure_app.Division'),
        ),
    ]