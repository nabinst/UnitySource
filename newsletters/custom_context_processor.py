from django.shortcuts import render, redirect
from .forms import NewsletterUserSignUpForm
from .models import NewsletterUser
from django.contrib import messages
#from django.views.generic import ListView
from blogs.models import Post
from django.http import HttpResponseRedirect


# Create your views here.

def  blog_post_latest(request):
    blog_latest = Post.objects.all().order_by('-date_posted')[0:3]
    
    return {'blog_latest_footer':blog_latest}
  