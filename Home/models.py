from django.db import models
from django.urls import reverse


class User(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

    def __str__(self):
        return str(self.id)+"."+self.username


class Photo(models.Model):
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length=500, default='')
    name = models.CharField(max_length=250, default='')

    def get_absolute_url(self):
        return reverse('share:detail', kwargs={'pk': self.pk})
