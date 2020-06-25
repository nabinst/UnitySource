from django import forms

class ContactForm(forms.Form):
    from_email = forms.EmailField( required=True, label='Email')
    subject = forms.CharField(max_length=100, required=True, label='Subject')
    message = forms.CharField(widget=forms.Textarea, required=True ,label='Message')


    def __init__(self, *args, **kwargs):
        super(ContactForm,self).__init__(*args,**kwargs)
        self.fields['from_email'].widget.attrs['placeholder']='Your Email'
        self.fields['subject'].widget.attrs['placeholder']='Subject'
        self.fields['message'].widget.attrs['placeholder']='Message'