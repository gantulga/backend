# Generated by Django 3.0.2 on 2020-02-19 09:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('structure_app', '0010_auto_20200215_1631'),
        ('product_app', '0007_auto_20200216_1935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commodity_transfer',
            old_name='quantity_balance',
            new_name='quantity',
        ),
        migrations.RenameField(
            model_name='commodity_transfer',
            old_name='quantity_deducted',
            new_name='size',
        ),
        migrations.RenameField(
            model_name='commodity_transfer',
            old_name='quantity_increased',
            new_name='unit_size',
        ),
        migrations.RemoveField(
            model_name='commodity_transfer',
            name='quantity_residuals',
        ),
        migrations.RemoveField(
            model_name='commodity_transfer',
            name='size_balance',
        ),
        migrations.RemoveField(
            model_name='commodity_transfer',
            name='size_deducted',
        ),
        migrations.RemoveField(
            model_name='commodity_transfer',
            name='size_increased',
        ),
        migrations.RemoveField(
            model_name='commodity_transfer',
            name='size_residuals',
        ),
        migrations.AlterField(
            model_name='commodity_transfer',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Commodity_balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('quantity', models.PositiveIntegerField()),
                ('size', models.PositiveIntegerField()),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='commodity_balances', to='structure_app.Client')),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='commodity_balances', to='product_app.Commodity')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='commodity_balance_createdby', to=settings.AUTH_USER_MODEL)),
                ('division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='commodity_balances', to='structure_app.Division')),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='commodity_balance_modifiedby', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='commodity_balances', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
