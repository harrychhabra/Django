# Generated by Django 2.1.2 on 2018-11-02 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0002_auto_20181031_1400'),
    ]

    operations = [
        migrations.RenameField(
            model_name='institute',
            old_name='institue_name',
            new_name='institute_name',
        ),
        migrations.RenameField(
            model_name='user_table',
            old_name='type',
            new_name='access_type',
        ),
        migrations.RenameField(
            model_name='user_table',
            old_name='institute_name',
            new_name='institute_name_user',
        ),
        migrations.AlterField(
            model_name='institute',
            name='user_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]