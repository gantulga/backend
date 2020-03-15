# Generated by Django 3.0.2 on 2020-02-11 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure_app', '0005_user_profile_avatar'),
        ('financial_app', '0002_auto_20200211_1723'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='structure_app.Client'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Pos_account_consolidation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('fr_date', models.DateTimeField()),
                ('to_date', models.DateTimeField()),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='financial_app.Wallet')),
                ('confirmed_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pos_account_consolidation_createdby', to=settings.AUTH_USER_MODEL)),
                ('person_of_charge', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='Pos_account_consolidations', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='pos_account_consolidation_modifiedby', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]