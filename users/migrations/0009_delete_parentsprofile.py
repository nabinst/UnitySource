# Generated by Django 3.0.7 on 2021-02-07 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_parentsprofile_position'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ParentsProfile',
        ),
    ]