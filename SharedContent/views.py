from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.urls import reverse
from Home.models import Photo
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import urls


class IndexView(generic.ListView):
    template_name = 'shared/List.html'
    context_object_name = 'all_photos'

    def get_queryset(self):
        return Photo.objects.all()


class DetailView(generic.DetailView):
    model = Photo
    template_name = 'shared/detail.html'

class PhotoCreate(CreateView):
    model = Photo
    fields = ['name']
'''def showphotolist (request):
    all_photos = Photo.objects.all()
    context = {
        'all_photos': all_photos,
    }
    return render(request, 'shared/List.html', context)


def showdetails (request, id):
    photo = get_object_or_404(Photo, pk=id)
    return render(request, 'shared/detail.html', {'photo': photo})


def homepage(request):

    return render(request, 'home/homepage.html')'''
