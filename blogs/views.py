from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.db.models import Count, Q
from django.core.paginator import Paginator

from .forms import BlogForm
from .models import Post, Category, Comment
from .forms import CommentForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, 
                                DetailView, 
                                CreateView, 
                                UpdateView,
                                DeleteView)
from hitcount.views import HitCountDetailView


# def get_category_count():
#     queryset = Post.objects.values('categories__title').annotate(Count('categories__title'))
#     return queryset

# def blog(request):
#     posts = Post.objects.all()
#     context ={
#         'posts': posts
#     }
#     return render (request, 'blog/blog.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blogs/blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6
    queryset = Post.objects.filter(featured=True).order_by('-date_posted')
    
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        #context_data['posts'] = Post.objects.filter(featured=True).order_by('-date_posted')
        context_data['blog_latest'] = Post.objects.filter(featured=True).order_by('-date_posted')[0:3]
        context_data['category_count'] = Post.objects.filter(featured=True).values('categories__title').annotate(Count('categories__title'))
        return context_data

class UserPostListView(ListView):
    model = Post
    template_name = 'blogs/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(featured=True).filter(author=user).order_by('-date_posted')

class CategoryPostListView(ListView):
    model = Post
    template_name = 'blogs/category_posts.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        category_id = self.kwargs['categories']
        category_list = Post.objects.filter(featured=True).filter(categories__title=category_id)
        return category_list

class PostDetailView(HitCountDetailView):
    model = Post
    template_name = 'blogs/blog-single.html'
    count_hit = True
    
    
    def get_context_data(self, **kwargs):

        context_data = super().get_context_data(**kwargs)
       
        comments = Paginator(self.object.comments.order_by('-timestamp'),6)
        page_number = self.request.GET.get('page')
        page_obj = comments.get_page(page_number)
        context_data['comments'] = page_obj
        context_data['page_obj'] = page_obj 

        #comments_connected = Comment.objects.filter(blogpost_connected=self.get_object()).order_by('-timestamp')[:6]
        #context_data['comments'] = comments_connected

        if self.request.user.is_authenticated:
            context_data['comment_form'] = CommentForm(instance=self.request.user)
        
        post =  self.get_object()
        context_data['blog_latest'] = Post.objects.filter(featured=True).order_by('-date_posted')[0:3]
       #context_data['comment'] = Comment.objects.filter(blogpost_connected=post)

        context_data['category_count'] = Post.objects.values('categories__title').annotate(Count('categories__title'))
        context_data['popular_posts'] = Post.objects.filter(featured=True).order_by('-hit_count_generic__hits')[:3]
        return context_data


    def post(self, request, *args, **kwargs):
        new_comment = Comment(content=request.POST.get('content'),
        user=self.request.user,
        blogpost_connected=self.get_object())
        new_comment.save()

        return self.get(self,request, *args, **kwargs)

    def get_success_url(self):
        return self.request.path



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = BlogForm
#     fields =['title','overview', 'content','thumbnail', 'categories','featured','previous_post',
# 'next_post']

    template_name = 'blogs/post_create.html'
  


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blog_latest'] = Post.objects.filter(featured=True).order_by('-date_posted')[0:3]
        context_data['name_title'] ='Create'
        return context_data

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = BlogForm
#     fields =['title','overview', 'content','thumbnail', 'categories','featured','previous_post',
# 'next_post']
    template_name = 'blogs/post_create.html'
    #title = 'Update'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blog_latest'] = Post.objects.filter(featured=True).order_by('-date_posted')[0:3]
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
    success_url = reverse_lazy('blog-home')
    template_name = 'blogs/post_delete.html'
    status = 'Delete'


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class CommentListView(ListView):
    model = Comment
    #paginate_by = 6


class CommentDetailView(DetailView):
    model = Comment
    #paginate_by = 6

    # def get_queryset(self):
  
    #     blog_comment_list = Comment.objects.filter(object__pk = self.object__pk)
    #     print(blog_comment_list)
    #     return blog_comment_list

    # def get_context_data(self, *kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     comments_connected = Comment.objects.filter(object__pk = self.object__pk).order_by('-timestamp')
    #     print(comments_connected)
    #     context_data['comments_list'] = comments_connected
    #     return context_data


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    
    #success_url = reverse_lazy('post-detail')
    #success_url = reverse_lazy('post-detail', kwargs={'pk':object.blogpost_connected.pk})

    #return reverse('post-detail', kwargs={'pk': self.pk})
    template_name = 'blogs/comment_delete.html'
    status = 'Delete'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.blogpost_connected.pk})
        
        

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False



def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')

    if query:
        queryset = queryset.filter(
            Q(title__icontains=query)|
            Q(overview__icontains=query)

        ).distinct()
    context = {
        'queryset': queryset
    }
    return render (request, 'blogs/search_results.html',context)