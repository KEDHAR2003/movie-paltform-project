# Generated by Django 4.1.7 on 2023-04-23 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0006_alter_moviedatails_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviedatails',
            name='image',
        ),
    ]
