from django.shortcuts import render, redirect
from .models import FormPdf
from .forms import PDFform
# Create your views here.


def list_pdf(request):
    pdf_lists = FormPdf.objects.all()
    context={
        'pdf_lists': pdf_lists
    }
    return render(request, 'pdf_files/pdf_list.html',context)


def upload_pdf(request):
    if request.method =="POST":
        form = PDFform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_pdf')
    else:
        form = PDFform()

    return render(request, 'pdf_files/upload_pdf.html',{
        'form':form
    })

def delete_pdf(request, pk):
    if request.method =='POST':
        pdf_file = FormPdf.objects.get(pk=pk)
        pdf_file.delete()
        return redirect('list_pdf')
    

