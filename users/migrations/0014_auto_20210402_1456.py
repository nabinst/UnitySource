# Generated by Django 3.0.7 on 2021-04-02 18:56

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_remove_profile_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, default='default.jpg', force_format='JPEG', keep_meta=True, quality=75, size=[800, 530], upload_to='profile_pics'),
        ),
    ]
