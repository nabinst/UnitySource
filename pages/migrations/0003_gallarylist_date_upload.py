# Generated by Django 3.0.7 on 2021-02-04 16:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20210204_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallarylist',
            name='date_upload',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
