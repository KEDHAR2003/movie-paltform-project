# Generated by Django 4.1.7 on 2023-04-26 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0011_moviedatails_viedo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedatails',
            name='viedo',
            field=models.FileField(default='', upload_to='movieviedo/%y'),
        ),
    ]
