from django.contrib import admin
from django.urls import path

from .views import contactView, successView

urlpatterns = [
    path('contact/', contactView, name='contact'),
    path('contact_success/', successView, name='contact_success'),
    #path('contact/',contactView, name='contact'),
    #path('contact_success/', successView, name='contact_success'),
]