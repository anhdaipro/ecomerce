# Generated by Django 3.2.4 on 2021-09-01 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0020_auto_20210901_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='phone_number',
        ),
    ]
