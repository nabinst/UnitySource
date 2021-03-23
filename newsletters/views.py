from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.views.generic import ListView , CreateView, DetailView, DeleteView, UpdateView
from .forms import NewsletterUserSignUpForm, NewsLetterCreationForm, EmailSignupForm
from .models import NewsletterUser, NewsLetter
from django.template.loader import render_to_string

from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError


from django.http import HttpResponseRedirect
import json
import requests

# Create your views here.

def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.success(request, f'You email already exists in our database.')
            return redirect('subscribe')
        else:
            instance.save()
            messages.success(request, f'Your email has been added to the database.')
            subject = "Thank you for Joining Our Newsleter"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]
            html_version = 'newsletters/subscribe_email.html'
            html_message = render_to_string(html_version)
            message = EmailMessage(subject, html_message,from_email, to_email)
            message.content_subtype = 'html'
            message.send()


            #signup_message = """ Welcome to Unity Center. If you would like to unsubscribe visit """
            #send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=signup_message,fail_silently=False)
           
            return redirect('subscribe')
    context ={
        'form':form
    }
    #return render(request, 'footer.html', context)
    return render(request, 'newsletters/subscribe.html', context)



class NewsCreateView(LoginRequiredMixin, CreateView):
    model = NewsLetter
    success_url = reverse_lazy('newsletter-list')
    fields = ['subject','body','email','status','attachment']

    

    def form_valid(self, form):
        instance = form.save()
        newsletter = NewsLetter.objects.get(id=instance.id)
        if newsletter.status == "Published":
            subject = newsletter.subject
            body = newsletter.body
            from_email = settings.EMAIL_HOST_USER
            email = ['clevelandunitycenter@gmail.com']
                # for email in newsletter.email.all():
            message = EmailMessage(subject, body,from_email, [email])
            #message.attach_file('/documents/Attachment.pdf')
            message.send()
            return super().form_valid(form)    
            #messages.success(request, f'Published')
            #return reverse_lazy('newsletter-list')
        else:
            messages.success(request, f'Draft Saved')
        return reverse_lazy('newsletter-list')
        #return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['name_title']= 'Create'
        return context_data


class NewsListView(ListView):
    model = NewsLetter
    ordering = ['-created']
    paginate_by = 8


class NewsDetailView(DetailView):
    model = NewsLetter


class NewsDeleteView(LoginRequiredMixin, DeleteView):
    model = NewsLetter

    success_url = reverse_lazy('newsletter-list')
    success_message = 'Item Deleted from the Newsletter List'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(NewsDeleteView, self).delete(request, *args, **kwargs)


class NewsUpdateView(LoginRequiredMixin, UpdateView): 
    model = NewsLetter
    fields =['subject','body','email','status','attachment']
   
    success_url = reverse_lazy('newsletter-list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['name_title']= 'Update'
        return context_data

   

       

# Mailchimp Settings

api_key = settings.MAILCHIMP_API_KEY
server  = settings.MAILCHIMP_DATA_CENTER
list_id  = settings.MAILCHIMP_EMAIL_LIST_ID

# aip_url =f'https://{MAILCHIMP_DATA_CENTER}.api.mailchimp.com/3.0/lists/{list_id}/members/{subscriber_hash}/notes/{id}'
api_url =f'https://{server}.api.mailchimp.com/3.0'
members_endpoint =f'{api_url}/lists/{list_id}/members'
members_endpoint_del =f'{api_url}/lists/{list_id}/members'


def subscribe(email):
    mailchimp = Client()
    mailchimp.set_config({
    "api_key":  api_key,
    "server": server
    })
    member_info = {
        "email_address": email,
        "status": "subscribed",
    }
    try:
        response = mailchimp.lists.add_list_member(list_id,member_info)
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))







def unsubscribe(email):
    mailchimp = Client()
    mailchimp.set_config({
    "api_key":  api_key,
    "server": server
    })
    member_info = {
        "email_address": email,
        "status": "subscribed",
    }
    try:
        response = mailchimp.lists.delete_list_member(list_id,email)
        print("response: {}".format(response))
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))



def email_list_signup(request):
    form = EmailSignupForm (request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            email_signup_qs = NewsletterUser.objects.filter(email= form.instance.email)
            if email_signup_qs.exists():
                messages.info(request, " You are alredy subscribed")
            else:
                subscribe(form.instance.email)
                form.save()
                messages.info(request, "Thank you for subscribing!")
                messages.success(request, f'Your email has been added to the database.')
                subject = "Thank you for Joining Our Newsleter"
                from_email = settings.EMAIL_HOST_USER
                to_email = [form.instance.email]
                html_version = 'newsletters/subscribe_email.html'
                html_message = render_to_string(html_version)
                message = EmailMessage(subject, html_message,from_email, to_email)
                message.content_subtype = 'html'
                message.send()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

            



def newsletter_unsubscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        email_signup_qs = NewsletterUser.objects.filter(email= instance.email)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
            unsubscribe(form.instance.email)
            messages.success(request, f'Your email has been deleted.')

            subject = "You have been unsubscribed"
            from_email = settings.EMAIL_HOST_USER
            to_email = [instance.email]

            html_version = 'newsletters/unsubscribe_email.html'
            html_message = render_to_string(html_version)
            message = EmailMessage(subject, html_message,from_email, to_email)
            message.content_subtype = 'html'
            message.send()


            #signup_message = """ Sorry to see you go. Let us know if there is an issue with our service."""
            #send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=signup_message,fail_silently=False)
            return redirect('unsubscribe')
        else:
            messages.success(request, f'Sorry but we did not find your email addres.')
            return redirect('unsubscribe')
    context={
        'form': form
    }
    return render(request, 'newsletters/unsubscribe.html',context)
