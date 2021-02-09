# Generated by Django 3.0.7 on 2021-02-04 16:21

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GallaryList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', django_resized.forms.ResizedImageField(crop=None, default='default.jpg', force_format='JPEG', keep_meta=True, quality=75, size=[500, 300], upload_to='gallary_pics')),
            ],
        ),
    ]
