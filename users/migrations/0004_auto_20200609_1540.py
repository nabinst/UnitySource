# Generated by Django 3.0.7 on 2020-06-09 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200609_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook',
            field=models.CharField(default='#', max_length=300),
        ),
        migrations.AddField(
            model_name='profile',
            name='google',
            field=models.CharField(default='#', max_length=300),
        ),
        migrations.AddField(
            model_name='profile',
            name='tweeter',
            field=models.CharField(default='#', max_length=300),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, help_text='MM/DD/YYYY', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='title',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]