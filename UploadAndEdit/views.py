from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from Home.models import Photo, User
from PIL import Image



def upload(request):

    context = {

    }
    return render(request, 'photo/upload.html', context)


def edit(request):
    if request.method == 'POST':
        uploaded_file=request.FILES['fileToUpload']
        photo = Photo()
        photo.uploader = User.objects.all()[0]
        photo.file = uploaded_file
        photo.save()
        context = {
            'photo': photo,
        }
        request.session['photo_pk'] = photo.pk

    return render(request, 'photo/edit.html', context)


def crop(request):

    return HttpResponse()


def bw(request):
    photo = Photo.objects.get(pk=request.session['photo_pk'])
    pil_image = Image.open(photo.file.url[1:])
    # black and white related code
    changed_image = pil_image.convert("L")
    changed_image.save(photo.file.url[1:])
    photo.save(update_fields=['file'])
    context = {
        'photo': photo,
    }
    return render(request, 'photo/edit.html', context)


def rotate(request):

    return HttpResponse()


def resize(request):

    return HttpResponse()

def share(request):

    return HttpResponse()
