from django.db import models

CAT_CHOICES = (
    ('future','FUTURE'),
    ('youth', 'YOUTH'),
    ('summer','SUMMER'),
    ('others','OTHERS'),
   )

class FormPdf(models.Model):
    title = models.CharField(max_length=100)
    overview = models.CharField(max_length=400)
    pdf = models.FileField(upload_to='pdfform/pdfs/')
    category = models.CharField(max_length=6, choices=CAT_CHOICES, default='others')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)