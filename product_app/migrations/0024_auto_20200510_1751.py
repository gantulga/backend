# Generated by Django 3.0.2 on 2020-05-10 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('structure_app', '0020_auto_20200509_1145'),
        ('product_app', '0023_auto_20200509_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_balance',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='item_balances', to='structure_app.Client'),
        ),
        migrations.AlterField(
            model_name='item_balance',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='item_balances', to='structure_app.Division'),
        ),
        migrations.AlterField(
            model_name='item_balance',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='item_balances', to=settings.AUTH_USER_MODEL),
        ),
    ]
