from django.db import models
from tinymce import HTMLField


# Create your models here.
class NewsletterUser(models.Model):
    email = models.EmailField()
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



class NewsLetter(models.Model):
    EMAIL_STATUS_CHOICES =(
        ('Draft', 'Draft'),
        ('Published', 'Published')
    ) 
    subject = models.CharField(max_length=250)
    body = HTMLField()
    #body = models.TextField()
    email = models.ManyToManyField(NewsletterUser)
    status = models.CharField(max_length=10, choices=EMAIL_STATUS_CHOICES)
    attachment = models.FileField(upload_to='newsletter/pdfs/', blank=True, null=True )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.subject

        