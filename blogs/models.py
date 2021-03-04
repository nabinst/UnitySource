from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from django.urls import reverse
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation



class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    content = HTMLField()
    date_posted =models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE )
    #view_count = models.IntegerField(default=0)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', 
    related_query_name='hit_count_generic_relation')
    thumbnail = models.ImageField()
    categories = models.ManyToManyField(Category)
    previous_post = models.ForeignKey('self', related_name ='previous',on_delete=models.SET_NULL, blank=True, null=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    @property
    def number_of_comments(self):
        return Comment.objects.filter(blogpost_connected=self).count()
   
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    blogpost_connected = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('comment-detail', kwargs={'blogpost_connected': self.blogpost_connected})