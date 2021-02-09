from django.db import models
from django_resized import ResizedImageField
from django.urls import reverse

#from PIL import Image

# Create your models here.
class GalleryList(models.Model):
    title = models.CharField(max_length=100)
    gallery_image = ResizedImageField(size=[800, 530], blank=True, null=True, upload_to='gallary_pics')
    date_upload =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

#    def get_absolute_url(self):
 #       return reverse('gallery-detail', kwargs={'pk':self.pk})
