from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from django.views.generic import ListView , CreateView, DetailView, DeleteView, UpdateView
from .forms import NewsletterUserSignUpForm, NewsLetterCreationForm
from .models import NewsletterUser, NewsLetter
from django.template.loader import render_to_string


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

def newsletter_unsubscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            NewsletterUser.objects.filter(email=instance.email).delete()
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

# def control_newsletter(request):
#     form = NewsLetterCreationForm(request.POST , request.FILES)
#     name_title = 'Create'
#     if request.method =="POST":
              
#         if form.is_valid():
#             instance = form.save()
#             newsletter = NewsLetter.objects.get(id=instance.id)
#             if newsletter.status == "Published":
#                 subject = newsletter.subject
#                 body = newsletter.body
#                 html_version = 'newsletters/control_newsletter.html'
#                 html_message = render_to_string(html_version)
#                 from_email = settings.EMAIL_HOST_USER
                
#                 for email in newsletter.email.all():
#                     message = EmailMessage(subject, html_message,from_email, [email])
#                     message.content_subtype = 'html'
#                     message.send()
#                     #send_mail(subject=subject, from_email=from_email, recipient_list=[email], message=body, fail_silently=False )
#                 #messages.success(request, f'Published')
#                 return reverse_lazy('newsletter-list')
#             else:
#                 messages.success(request, f'Draft Saved')
#                 return reverse_lazy('newsletter-list')
    
#     context ={
#         "form": form,
#         "name_title": name_title,
#     }   
#     return render(request, 'newsletters/control_newsletter.html', context)


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

   

       


    