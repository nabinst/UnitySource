# Generated by Django 3.0.7 on 2021-03-28 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20210327_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user_email',
        ),
    ]