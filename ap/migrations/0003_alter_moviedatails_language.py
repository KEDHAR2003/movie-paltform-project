# Generated by Django 4.1.7 on 2023-04-23 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ap', '0002_moviedatails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviedatails',
            name='language',
            field=models.CharField(choices=[('te', 'telugu'), ('en', 'english'), ('ta', 'tamil'), ('hn', 'hindi'), ('ka', 'kanada'), ('al', 'all')], max_length=2),
        ),
    ]
