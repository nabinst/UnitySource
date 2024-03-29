from django.db import models
from django.urls import reverse
from tinymce import HTMLField
from django_resized import ResizedImageField


class ParentsProfile(models.Model):
    name = models.CharField(max_length=100)
    parent_image = ResizedImageField(size=[200, 200], default='default.jpg', upload_to='parent_pics')
    comment = models.TextField(max_length=500, blank=True)
    user_parent = models.BooleanField(default=False)
    position = models.CharField(max_length=100, blank=True, default='Parent')
    date_posted =models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)


class OrgFacts(models.Model):
    facts_category = models.CharField(max_length=150)
    counts = models.IntegerField()
    
class Future(models.Model):
    title = models.CharField(max_length=100)
    image = ResizedImageField(size=[500, 400],  blank=False, null=False, upload_to='future_pics')
    overview = models.TextField(max_length=300)
    content = HTMLField()
    duration = models.CharField(max_length=100, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now=True)
    sort = models.IntegerField(default=99)

    def __str__(self):
            return self.title
    
    def get_absolute_url(self):
        return reverse('future-detail', kwargs={'pk': self.pk})


class Youth(models.Model):
    title = models.CharField(max_length=100)
    image = ResizedImageField(size=[500, 400],  blank=False, null=False ,upload_to='youth_pics')
    overview = models.TextField(max_length=300)
    content = HTMLField()
    duration = models.CharField(max_length=100, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now=True)
    sort = models.IntegerField(default=99)

    def __str__(self):
            return self.title
    
    def get_absolute_url(self):
        return reverse('youth-detail', kwargs={'pk': self.pk})


class Summer(models.Model):
    title = models.CharField(max_length=100)
    image = ResizedImageField(size=[500, 400], blank=False, null=False, upload_to='summer_pics')
    overview = models.TextField(max_length=300)
    content = HTMLField()
    duration = models.CharField(max_length=100, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now=True)
    sort = models.IntegerField(default=99)

    def __str__(self):
            return self.title
    
    def get_absolute_url(self):
        return reverse('summer-detail', kwargs={'pk': self.pk})

class Volunteers(models.Model):
    title = models.CharField(max_length=100)
    image = ResizedImageField(size=[500, 400],  blank=False, null=False, upload_to='youth_pics')
    overview = models.TextField(max_length=300)
    content = HTMLField()
    duration = models.CharField(max_length=100, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=False)
    date_updated = models.DateTimeField(auto_now=True)
    sort = models.IntegerField(default=99)
    
    def __str__(self):
            return self.title
    
    def get_absolute_url(self):
        return reverse('volunteers-detail', kwargs={'pk': self.pk})