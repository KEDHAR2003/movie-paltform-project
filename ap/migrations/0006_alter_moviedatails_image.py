# Generated by Django 4.1.7 on 2023-04-23 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0005_remove_moviedatails_videofile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedatails',
            name='image',
            field=models.ImageField(upload_to='moviedatails'),
        ),
    ]