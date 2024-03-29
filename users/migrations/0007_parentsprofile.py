# Generated by Django 3.0.7 on 2021-02-07 04:02

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_profile_user_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParentsProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('parent_image', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, size=[200, 200], upload_to='parent_pics')),
                ('comment', models.TextField(blank=True, max_length=500)),
                ('user_parent', models.BooleanField(default=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
