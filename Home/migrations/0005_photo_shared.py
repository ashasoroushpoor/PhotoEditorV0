# Generated by Django 2.1.5 on 2019-02-12 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_auto_20190212_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='shared',
            field=models.BooleanField(default=False),
        ),
    ]
