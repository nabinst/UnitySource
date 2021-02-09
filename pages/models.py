from django.db import models
from django_resized import ResizedImageField


class ParentsProfile(models.Model):
    name = models.CharField(max_length=100)
    parent_image = ResizedImageField(size=[200, 200], blank=True, null=True, upload_to='parent_pics')
    comment = models.TextField(max_length=500, blank=True)
    user_parent = models.BooleanField(default=True)
    position = models.CharField(max_length=100, blank=True, default='Parent')
    date_posted =models.DateTimeField(auto_now_add=True)


class OrgFacts(models.Model):
    facts_category = models.CharField(max_length=150)
    counts = models.IntegerField()
    