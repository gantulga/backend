# Generated by Django 3.0.2 on 2020-05-03 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0015_auto_20200503_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_transfer',
            name='size_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='item_transfers', to='product_app.Size_type'),
            preserve_default=False,
        ),
    ]
