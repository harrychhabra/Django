# Generated by Django 2.1.2 on 2018-11-03 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0005_auto_20181103_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_table',
            name='profile_pic_path',
            field=models.ImageField(default='samvad\\media\x08ig.jpg', upload_to='profile_pic'),
        ),
    ]
