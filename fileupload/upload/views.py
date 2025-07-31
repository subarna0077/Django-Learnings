from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import FileUpload
from django.urls import reverse_lazy


# Create your views here.

class FileUploadView(CreateView):
    model = FileUpload
    fields = ['title', 'image']
    template_name = 'upload/upload_form.html'
    success_url = reverse_lazy('file-upload')

