from django.db import models
from django_resized import ResizedImageField
from django.urls import reverse

#from PIL import Image

# Create your models here.
class GalleryList(models.Model):
    PIC_CAT_CHOICES =(
        ('Event', 'Event'),
        ('Summer', 'Summer'),
        ('Future', 'Future'),
        ('Building', 'Building'),
        ('About', 'About'),
        ('Volunteers', 'Volunteers'),
        ('Youth Leadership', 'Youth Leadership'),
        ('Gallary', 'Gallary')
        )
    title = models.CharField(max_length=100)
    gallery_image = ResizedImageField(size=[800, 530], blank=False, null=False, upload_to='gallary_pics')
    date_upload =models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=True)
    pic_cat = models.CharField(max_length=30, choices=PIC_CAT_CHOICES, default='Gallary')

    def __str__(self):
        return self.title

#    def get_absolute_url(self):
 #       return reverse('gallery-detail', kwargs={'pk':self.pk})
