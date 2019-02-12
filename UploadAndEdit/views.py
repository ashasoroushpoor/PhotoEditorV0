from django.shortcuts import render
from django.http import  HttpResponse


def uploadpage(request):
    context = {

    }
    return render(request, 'photo/upload.html', context)


def upload(request):

    return HttpResponse(request.POST['fileToUpload'])
