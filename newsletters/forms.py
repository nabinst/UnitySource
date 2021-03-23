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


class EmailSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        "type": "email",
        "name": "email",
        "id": "email",
        "placeholder": "Enter email address",
        "class": "form-control mb-2 text-center"
    }), label="")
    class Meta:
        model = NewsletterUser
        fields = ('email',)
