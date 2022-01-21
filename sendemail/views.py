from django.shortcuts import render, redirect
from .forms import ContactForm
from blogs.models import Post
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

def contactView(request):
    if request.method =='GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            msg_mail = str(message) + "\nFrom: " + str(from_email)

            try:
                send_mail(subject, msg_mail, from_email, ['clevelandunitycenter@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact_success')

    blog_latest = Post.objects.filter(featured=True).order_by('-date_posted')[0:3]

    context = {
        'form': form,
        'blog_latest': blog_latest
    }
    return render(request, 'send_email/contact.html', context)

def successView(request):
    return render(request, 'send_email/contact_success.html',{})
    #HttpResponse('Success! Thank you for your message.')


# email = EmailMessage(
#     subject=subject,
#     body=message,
#     from_email=email_from,
#     to=[email_to],
#     reply_to=[email_from],
# )

# email.send()