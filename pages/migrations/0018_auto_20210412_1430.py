# Generated by Django 3.0.7 on 2021-04-12 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_future_sort'),
    ]

    operations = [
        migrations.AddField(
            model_name='summer',
            name='sort',
            field=models.IntegerField(default=99),
        ),
        migrations.AddField(
            model_name='volunteers',
            name='sort',
            field=models.IntegerField(default=99),
        ),
        migrations.AddField(
            model_name='youth',
            name='sort',
            field=models.IntegerField(default=99),
        ),
    ]