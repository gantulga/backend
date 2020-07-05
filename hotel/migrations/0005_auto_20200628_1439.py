# Generated by Django 3.0.2 on 2020-06-28 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0004_auto_20200628_1404'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel_client_log',
            name='choices',
        ),
        migrations.AddField(
            model_name='hotel_client_log',
            name='choices_type',
            field=models.CharField(choices=[('1', 'Өрөөний мэдээлэл'), ('2', 'Зочины тоон мэдээлэл'), (
                '3', 'Цэвэрлэгээний мэдээлэл'), ('4', 'Мини барны мэдээлэл')], max_length=3),
            preserve_default=False,
        ),
    ]