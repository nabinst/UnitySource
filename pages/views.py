from django.shortcuts import render, get_object_or_404
from users.models import Profile
from blogs.models import Post 
from django.views.generic import ListView




class IndexView(ListView):
    template_name = 'pages/index.html'
    context_object_name = 'index'
    model = Profile
    
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['teacher_latest'] = Profile.objects.filter(teacher=True).order_by('?')[0:4]
        context_data['teacher_count'] = Profile.objects.all().count()
        context_data['blog_latest'] = Post.objects.all().order_by('-date_posted')[0:3]
        #teacher_count = Profile.objects.all().count()
        #teacher_latest = Profile.objects.filter(teacher=True).order_by('?')[0:4]
        #featured = Post.objects.filter(featured=True)
        #latest = Post.objects.order_by('-timestamp')[0:3]
        return context_data


class AboutListView(ListView):
    template_name = 'pages/about.html'
    model = Post
    context_object_name = 'about'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blog_latest'] = Post.objects.all().order_by('-date_posted')[0:3]
        return context_data

class TeacherListView(ListView):
    template_name = 'pages/teacher.html'
    model = Post

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['teachers'] = Profile.objects.filter(user_staff=True)
        context_data['blog_latest'] = Post.objects.all().order_by('-date_posted')[0:3]
        return context_data

class PricingListView(ListView):
    template_name = 'pages/pricing.html'
    model = Post

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blog_latest'] = Post.objects.all().order_by('-date_posted')[0:3]
        return context_data

class CoursesListView(ListView):
    template_name = 'pages/courses.html'
    model = Post

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blog_latest'] = Post.objects.all().order_by('-date_posted')[0:3]
        return context_data




