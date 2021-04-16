from django.shortcuts import render, get_object_or_404
from users.models import Profile
from blogs.models import Post 
from django.views.generic import ListView, DetailView
from gallery.models import GalleryList
from .models import ParentsProfile, OrgFacts, Future, Youth, Summer, Volunteers


class IndexView(ListView):
    template_name = 'pages/index.html'
    context_object_name = 'index'
    model = Profile
    
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['teacher_latest'] = Profile.objects.filter(featured=True).order_by('?')[0:4]
        context_data['teacher_count'] = Profile.objects.all().count()
        context_data['blog_latest'] = Post.objects.filter(featured=True).order_by('-date_posted')[0:3]
        #teacher_count = Profile.objects.all().count()
        #teacher_latest = Profile.objects.filter(teacher=True).order_by('?')[0:4]
        #featured = Post.objects.filter(featured=True)
        #latest = Post.objects.order_by('-timestamp')[0:3]
        context_data['galary_pic'] = GalleryList.objects.all().order_by('-date_upload')[0:4]
        context_data['parent_comment'] = ParentsProfile.objects.filter(featured=True).order_by('-date_posted')[0:6]
        context_data['future_program'] = Future.objects.filter(featured=True).order_by('-date_posted')[0:6]
        context_data['youth_program'] = Youth.objects.filter(featured=True).order_by('-date_posted')[0:4]
        context_data['org_fact'] = OrgFacts.objects.all()
        return context_data


class AboutListView(ListView):
    template_name = 'pages/about.html'
    model = Post
    context_object_name = 'about'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        #context_data['blog_latest'] = Post.objects.all().order_by('-date_posted')[0:3]
        context_data['galary_pic'] = GalleryList.objects.all().order_by('-date_upload')[0:4]
        context_data['parent_comment'] = ParentsProfile.objects.filter(featured=True).order_by('-date_posted')[0:6]
        context_data['teacher_count'] = Profile.objects.all().count()
        context_data['teacher_latest'] = Profile.objects.filter(featured=True).order_by('?')[0:4]
        context_data['org_fact'] = OrgFacts.objects.all()
        return context_data

class TeacherListView(ListView):
    template_name = 'pages/teacher.html'
    model = Post

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['teachers'] = Profile.objects.filter(featured=True)
        context_data['blog_latest'] = Post.objects.filter(featured=True).order_by('-date_posted')[0:3]
        return context_data

class PricingListView(ListView):
    template_name = 'pages/pricing.html'
    model = Post

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blog_latest'] = Post.objects.filter(featured=True).order_by('-date_posted')[0:3]
        return context_data

class CoursesListView(ListView):
    template_name = 'pages/courses.html'
    model = Post

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['blog_latest'] = Post.objects.filter(featured=True).order_by('-date_posted')[0:3]
        return context_data


def CalendarView(request):
    return render(request, 'pages/calendar.html',{})


class FutureListView(ListView):
    model = Future
    ordering = 'sort'

class FutureDetailView(DetailView):
    model = Future
    
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['future_list'] = Future.objects.filter(featured=True).order_by('sort')
        return context_data


class YouthListView(ListView):
    model = Youth
    ordering = 'sort'

class YouthDetailView(DetailView):
    model = Youth

    def get_context_data(self, **kwargs):
            context_data = super().get_context_data(**kwargs)
            context_data['youth_list'] = Youth.objects.filter(featured=True).order_by('sort')
            return context_data

class SummerListView(ListView):
    model = Summer
    ordering = 'sort'


class SummerDetailView(DetailView):
    model = Summer
   
    def get_context_data(self, **kwargs):
            context_data = super().get_context_data(**kwargs)
            context_data['summer_list'] = Summer.objects.filter(featured=True).order_by('sort')
            return context_data

class VolunteersListView(ListView):
    model = Volunteers
    ordering = 'sort'
    
class VolunteersDetailView(DetailView):
    model = Volunteers
 
    def get_context_data(self, **kwargs):
            context_data = super().get_context_data(**kwargs)
            context_data['volunteer_list'] = Volunteers.objects.filter(featured=True).order_by('sort')
            return context_data

class PartnersListView(ListView):
    model = Volunteers
    template_name = 'pages/partner_list.html'
    ordering = '-date_updated'

class FacilitiesListView(ListView):
    model = Volunteers
    template_name = 'pages/facilities_list.html'

    # def get_context_data(self, **kwargs):
    #     context_data = super().get_context_data(**kwargs)
    #     context_data['facility_list'] = GalleryList.objects.filter(pic_cat='Building').order_by('-date_upload')
    #     return context_data