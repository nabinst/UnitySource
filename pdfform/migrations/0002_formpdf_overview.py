# Generated by Django 3.0.7 on 2020-06-24 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formpdf',
            name='overview',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
