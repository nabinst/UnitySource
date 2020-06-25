from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, 
                                DetailView, 
                                CreateView, 
                                UpdateView,
                                DeleteView)

def blog(request):
    posts = Post.objects.all()
    context ={
        'posts': posts
    }
    return render (request, 'blog/blog.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blog_latest'] = Post.objects.all().order_by('-date_posted')[0:3]
        return context_data

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/blog-single.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields =['title','overview', 'content','thumbnail']
    template_name = 'blog/post_create.html'
  


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blog_latest'] = Post.objects.all().order_by('-date_posted')[0:3]
        context_data['name_title'] ='Create'
        return context_data

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields =['title','overview', 'content','thumbnail']
    template_name = 'blog/post_create.html'
    title = 'Update'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blog_latest'] = Post.objects.all().order_by('-date_posted')[0:3]
        context_data['name_title'] ='Update'
        return context_data

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'blog/post_delete.html'
    status = 'Delete'


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False