# Generated by Django 3.0.7 on 2021-03-27 20:11

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_auto_20210301_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[800, 530], upload_to='post_pics'),
        ),
    ]
