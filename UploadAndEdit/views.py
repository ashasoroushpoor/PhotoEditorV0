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
    photo = Photo.objects.get(pk=request.session['photo_pk'])
    pil_image = Image.open(photo.file.url[1:])
    changed_image = pil_image.crop((int(request.POST.get('left')),
                                    int(request.POST.get('upper')),
                                    int(request.POST.get('right')),
                                    int(request.POST.get('lower'))))
    changed_image.save(photo.photo.url[1:])
    photo.save(update_fields=['file'])
    context = {
        'photo': photo,
    }
    return render(request, 'photo/edit.html', context)


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
    photo = Photo.objects.get(pk=request.session['photo_pk'])
    pil_image = Image.open(photo.file.url[1:])
    changed_image = pil_image.rotate(int(request.POST.get('angle')),
                                     expand=1)
    changed_image.save(photo.file.url[1:])
    photo.save(update_fields=['file'])
    context = {
        'photo': photo,
    }
    return render(request, 'photo/edit.html', context)


def resize(request):
    photo = Photo.objects.get(pk=request.session['photo_pk'])
    pil_image = Image.open(photo.file.url[1:])
    changed_image = pil_image.resize((int(request.POST.get('width')),
                                      int(request.POST.get('height'))))
    changed_image.save(photo.file.url[1:])
    photo.save(update_fields=['file'])
    context = {
        'photo': photo,
    }
    return render(request, 'photo/edit.html', context)


def share(request):
    photo = Photo.objects.get(pk=request.session['photo_pk'])
    pil_image = Image.open(photo.file.url[1:])
    photo.shared = True
    photo.save(update_fields=['shared'])
    context = {
        'photo': photo,
    }
    return render(request, 'photo/edit.html', context)
