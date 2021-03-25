# Generated by Django 3.0.7 on 2021-03-19 23:07

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0003_newsletter_attachment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='newsletter/pdfs/'),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='body',
            field=tinymce.models.HTMLField(),
        ),
    ]