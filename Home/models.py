from django.db import models
from django.urls import reverse


class User(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

    def __str__(self):
        return str(self.id)+"."+self.username


class Photo(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=25000, default='')
    file = models.ImageField(default='')
    shared = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('share:detail', kwargs={'pk': self.pk})
