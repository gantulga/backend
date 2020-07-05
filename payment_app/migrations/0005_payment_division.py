# Generated by Django 3.0.2 on 2020-07-04 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure_app', '0002_auto_20200621_1448'),
        ('payment_app', '0004_remove_payment_division'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='payments', to='structure_app.Division'),
        ),
    ]
