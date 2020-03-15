# Generated by Django 3.0.2 on 2020-03-13 15:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel_client_log',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='hotel_client_log',
            name='limit_time',
        ),
        migrations.RemoveField(
            model_name='hotel_client_log',
            name='start_time',
        ),
        migrations.AddField(
            model_name='hotel_client_log',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hotel_client_log',
            name='number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='hotel_client_log',
            name='room_info_choices',
            field=models.CharField(choices=[('0', '---'), ('in', 'Зочинтой'), ('out', 'Сул')], default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='hotel_client_log',
            name='choices_type',
            field=models.CharField(choices=[('1', 'Өрөөний мэдээлэл'), ('2', 'Зочины тоон мэдээлэл'), ('3', 'Цэвэрлэгээний мэдээлэл'), ('4', 'Мини барны мэдээлэл')], max_length=3),
        ),
    ]