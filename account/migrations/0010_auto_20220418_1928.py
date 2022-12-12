# Generated by Django 3.2.4 on 2022-04-18 12:28

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20220418_1834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None),
        ),
        migrations.AlterField(
            model_name='smsverification',
            name='time_st',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
