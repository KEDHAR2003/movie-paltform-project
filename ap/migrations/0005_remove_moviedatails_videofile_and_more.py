# Generated by Django 4.1.7 on 2023-04-23 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0004_moviedatails_videofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviedatails',
            name='videofile',
        ),
        migrations.AlterField(
            model_name='moviedatails',
            name='image',
            field=models.ImageField(upload_to='moviedetails'),
        ),
    ]
