# Generated by Django 3.0.2 on 2020-02-15 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure_app', '0010_auto_20200215_1631'),
        ('product_app', '0003_auto_20200213_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='division_products', to='structure_app.Division'),
        ),
        migrations.AlterField(
            model_name='product',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='client_products', to='structure_app.Client'),
        ),
    ]