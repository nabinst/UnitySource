# Generated by Django 3.0.7 on 2021-06-21 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0004_auto_20210319_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='attachment',
            field=models.FileField(default=2019, upload_to='newsletter/pdfs/'),
            preserve_default=False,
        ),
    ]
