# Generated by Django 3.2.4 on 2022-04-28 10:18

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myweb', '0004_notify_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='image_home',
            name='upload_by',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
