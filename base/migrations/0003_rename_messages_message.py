# Generated by Django 3.2.6 on 2022-06-18 17:54

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0002_auto_20220618_1252'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Messages',
            new_name='Message',
        ),
    ]
