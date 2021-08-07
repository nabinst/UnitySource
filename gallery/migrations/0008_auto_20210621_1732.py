# Generated by Django 3.0.7 on 2021-06-21 21:32

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20210307_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallerylist',
            name='gallery_image',
            field=django_resized.forms.ResizedImageField(crop=None, default='2021/01/01', force_format='JPEG', keep_meta=True, quality=75, size=[800, 530], upload_to='gallary_pics'),
            preserve_default=False,
        ),
    ]
