# Generated by Django 3.2.4 on 2022-04-19 11:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20220419_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='smsverification',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 19, 11, 49, 25, 466615, tzinfo=utc)),
        ),
    ]
