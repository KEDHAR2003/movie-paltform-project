# Generated by Django 4.1.7 on 2023-04-23 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0007_remove_moviedatails_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviedatails',
            name='image',
            field=models.ImageField(default='', upload_to='moviedatails'),
        ),
    ]
