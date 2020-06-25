from django import forms
from .models import FormPdf

class PDFform(forms.ModelForm):
    class Meta:
        model = FormPdf
        fields = ('title', 'overview','pdf')