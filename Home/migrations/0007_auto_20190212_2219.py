# Generated by Django 2.1.5 on 2019-02-12 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_auto_20190212_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='shared',
            field=models.BooleanField(default=True),
        ),
    ]
