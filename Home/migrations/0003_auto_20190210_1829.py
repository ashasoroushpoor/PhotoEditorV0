# Generated by Django 2.1.5 on 2019-02-10 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_photo_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='nameId',
        ),
        migrations.AddField(
            model_name='photo',
            name='filename',
            field=models.CharField(default='', max_length=500),
        ),
    ]
