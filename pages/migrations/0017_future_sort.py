# Generated by Django 3.0.7 on 2021-04-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20210329_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='future',
            name='sort',
            field=models.IntegerField(default=99),
        ),
    ]