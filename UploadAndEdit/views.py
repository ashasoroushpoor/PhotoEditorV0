from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from Home.models import Photo,User


def upload(request):

    context = {

    }
    return render(request, 'photo/upload.html', context)


def edit(request):
    if request.method == 'POST':
        uploaded_file=request.FILES['fileToUpload']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        context = {
            'file_url': url
        }
        photo = Photo()
        photo.uploader = User.objects.all()[0]
        photo.file = url
        photo.save()
    return render(request, 'photo/edit.html', context)
