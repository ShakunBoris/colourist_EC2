from django.shortcuts import render
from django.urls import reverse
from .forms import *
from os import listdir
from pathlib import Path
from .models import GalleryImage
from .parsing_vimeo import list_of_videos
# Create your views here.

def index(request):
    return render(request, 'front/index.html', {})

def gallery(request):
    imgs = GalleryImage.objects.all()
    context = {
        'imgs': imgs,
    }
    return render(request, 'front/gallery.html', context)

def director(request):
    context = {
        'videos': list_of_videos(),
    }
    return render(request, 'front/director.html', context)

def contact(request):
    if request.method =="POST":
        form = ApplicationForm(request.POST)
        if  form.is_valid():
            form.save()
            return render(request, 'front/contact.html', {
                'form': form,
                'success': 'Success!',
                })
        else:
            return render(request, 'front/contact.html', {
                'form': form,
                'success': 'something went wrong...'
                })
    return render(request, 'front/contact.html', {
            'form': ApplicationForm()
            })