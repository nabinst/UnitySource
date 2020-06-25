from django.db import models

class FormPdf(models.Model):
    title = models.CharField(max_length=100)
    overview = models.CharField(max_length=400)
    pdf = models.FileField(upload_to='pdfform/pdfs/')

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)