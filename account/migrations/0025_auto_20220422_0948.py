# Generated by Django 3.2.4 on 2022-04-22 02:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_auto_20220422_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2022, 4, 22, 9, 47, 53, 326539), null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='no_user_c5clxa.png', upload_to=''),
        ),
    ]
