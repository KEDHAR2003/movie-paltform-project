from django.db import models

# Create your models here.
LANGUAGE_CHOICE=(
    ('te','telugu'),
    ('en','english'),
    ('ta','tamil'),
    ('hn','hindi'),
    ('ka','kanada'),
    ('al','all')
)

CATEGORY_CHOICE=(
    ('ac','action'),
    ('rc','romance'),
    ('co','comedy'),
    ('hr','horror'),
    ('ad','adventures'),
    ('ms','mystery'),
    ('th','thriller'),
)


class Regestration(models.Model):
    firstname=models.CharField(max_length=64)
    secondname=models.CharField(max_length=64)
    email=models.EmailField(max_length=64,unique=True,default='')
    city=models.CharField(max_length=64)


class moviedatails(models.Model):
    title=models.CharField(max_length=64)
    language=models.CharField(choices=LANGUAGE_CHOICE,max_length=2)
    category=models.CharField(choices=CATEGORY_CHOICE,max_length=64)
    cast=models.TextField(default='')
    description=models.TextField()
    image=models.ImageField(upload_to='moviedatails/%y',default='')
    viedo=models.FileField(upload_to='play//%y', default='')
