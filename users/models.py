from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from django.utils.translation import gettext as _


class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    title = models.CharField( max_length=30, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True, help_text='YYYY-MM-DD')
    user_staff = models.BooleanField(default=False)
    teacher = models.BooleanField(default=False)
    facebook = models.CharField( max_length=300, blank=True,default='#')
    google = models.CharField( max_length=300, blank=True,default='#')
    tweeter = models.CharField( max_length=300, blank=True,default='#')
    
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
      
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
       
        # try:
        #     old_img = Profile.objects.get(id=self.id)
        #     if old_img.image != self.image.path:
        #         old_img.image.delete(save=False)
        # except: pass

        if img.height > 200 or img.width > 200:
            output_size =(200,200)
            img.thumbnail(output_size)
            img.save(self.image.path)
    
        