# Generated by Django 2.1.5 on 2019-02-12 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_photo_shared'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='name',
        ),
        migrations.AddField(
            model_name='photo',
            name='caption',
            field=models.CharField(default='', max_length=25000),
        ),
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]