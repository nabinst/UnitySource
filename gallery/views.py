from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from .models import GalleryList
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

class GalleryListView(ListView):
    model = GalleryList
    ordering = ['-date_upload']
    paginate_by = 8

class GalleryCreateView(SuccessMessageMixin,LoginRequiredMixin,CreateView):
    model = GalleryList
    fields =['title', 'gallery_image']
    success_url = reverse_lazy('gallery-list')
    success_message = 'Picture added to the Gallery'

class GalleryDeleteView(LoginRequiredMixin, DeleteView):
    model = GalleryList
    success_url = reverse_lazy('gallery-list')
    success_message = 'Item Deleted from the Gallery'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(GalleryDeleteView, self).delete(request, *args, **kwargs)

class FacilitiesListView(ListView):
    model = GalleryList
    template_name = 'gallery/facilities_list.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['facility_list'] = GalleryList.objects.filter(pic_cat='Building').order_by('-date_upload')
        return context_data