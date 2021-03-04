from django import forms
from .models import NewsletterUser, NewsLetter
from crispy_forms.helper import FormHelper



class NewsletterUserSignUpForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = False
   

    
    class Meta:
        model = NewsletterUser
        fields = ['email']

        def clean_email(self):
            email = self.cleaned_data.get('email')
            return email


class NewsLetterCreationForm(forms.ModelForm):

    class Meta:
        model = NewsLetter
        fields =['subject','body','email','status','attachment']


