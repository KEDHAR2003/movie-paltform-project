# Generated by Django 4.1.7 on 2023-05-25 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0015_alter_regestration_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regestration',
            name='email',
            field=models.EmailField(max_length=64),
        ),
    ]
