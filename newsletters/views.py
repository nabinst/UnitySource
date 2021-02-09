from django.shortcuts import render, redirect
from .forms import NewsletterUserSignUpForm
from .models import NewsletterUser
from django.contrib import messages


# Create your views here.

def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsletterUser.objects.filter(email=instance.email).exists():
            messages.success(request, f'You email already existed.')
            return redirect('subscribe')
        else:
            instance.save()
            messages.success(request, f'Your email has been added.')
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
            return redirect('unsubscribe')
        else:
            messages.success(request, f'Sorry but we did not find your email addres.')
            return redirect('unsubscribe')
    context={
        'form': form
    }
    return render(request, 'newsletters/unsubscribe.html',context)