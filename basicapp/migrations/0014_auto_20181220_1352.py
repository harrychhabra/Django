# Generated by Django 2.1.2 on 2018-12-20 13:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basicapp', '0013_auto_20181220_1323'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='user_interest',
            unique_together={('user_name', 'interest_name')},
        ),
    ]
