from django.shortcuts import render
from .models import Regestration,moviedatails
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request,"ap/index.html")

def signup(request):

    if request.method=="POST":
        firstname=request.POST['fname']
        secondname=request.POST['sname']
        email=request.POST['email']
        city=request.POST['city']
        details=Regestration(firstname=firstname,secondname=secondname,email=email,city=city)

        details.save()

        username=request.POST['username']
        password=request.POST['pass']
        firstname=request.POST['fname']
        lastname=request.POST['sname']
        email=request.POST['email']

        myuser=User.objects.create_user(username=username,password=password)
        
        myuser.save()
        return render(request,"ap/signin.html")

    return render(request,"ap/signup.html")

def signin(request):

    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse(home))

        else:
            return render(request,'ap/signin.html',{
            "message":"invalid credientails"})
    return render(request,'ap/signin.html')

def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse(signin))
    elif(request.user.is_superuser==True):
        return render(request,"ap/normaluser.html")

    else:    
        movie=moviedatails.objects.all()
        return render(request,"ap/home.html",locals())

def signout(request):
    logout(request)
    return render(request,"ap/signin.html",{
        'message':'successfully logeedout'
    })
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse(signin))

   


def moviedetails(request,pk):
    movie=moviedatails.objects.get(pk=pk)
    return render(request,"ap/moviedetails.html",locals())




def play(request,pk):
    movie=moviedatails.objects.get(pk=pk)
    return render(request,"ap/play.html",locals())


def userdetails(request):
    uder=Regestration.objects.all()
    return render(request,"ap/userdetails.html",locals())

def movielist(request):
    movie=moviedatails.objects.all()
    return render(request,"ap/movielist.html",locals())


def normaluser(request):
    if request.method=="POST":
        firstname=request.POST['fname']
        secondname=request.POST['sname']
        email=request.POST['email']
        city=request.POST['city']
        details=Regestration(firstname=firstname,secondname=secondname,email=email,city=city)

        details.save()

        username=request.POST['username']
        password=request.POST['pass']
        firstname=request.POST['fname']
        lastname=request.POST['sname']
        email=request.POST['email']

        myuser=User.objects.create_user(username=username,password=password,email=email)
        myuser.first_name=firstname
        myuser.last_name=lastname

        
        myuser.save()
        uder=Regestration.objects.all()
        return render(request,"ap/userdetails.html",locals())
    return render(request,"ap/normaluser.html")


def language(request,value):
    movie=moviedatails.objects.filter(language=value)

    return render(request,"ap/language.html",locals())


def category(request,value):
    movie=moviedatails.objects.filter(category=value)
    return render(request,"ap/category.html",locals())


def delete(request,value):
    men=Regestration.objects.get(firstname=value)
    men.delete()
    user=User.objects.get(first_name=value)
    user.delete()
    return render(request,"ap/delete.html",locals())


def mdelete(request,pk):
    men=moviedatails.objects.get(pk=pk)
    men.delete()
    return render(request,"ap/delete.html",locals())

def update(request,value):
    men=Regestration.objects.get(secondname=value)
    men1=User.objects.get(last_name=value)
    return render(request,"ap/update.html",locals())


def upuser(request,value):
    men=Regestration.objects.get(secondname=value)
    men1=User.objects.get(last_name=value)
    uder=Regestration.objects.all()
    if request.method=="POST":
        firstname=request.POST['firstname']
        secondname=request.POST['secondname']
        username=request.POST['username']
        email=request.POST['email']
        city=request.POST['city']
        men.firstname=firstname
        men.secondname=secondname
        men.email=email
        men.city=city

        men.save()

        men1.first_name=firstname
        men1.username=username
        men1.last_name=secondname
        men1.email=email

        men1.save()
        return render(request,"ap/userdetails.html",locals())
    return render(request,"ap/userdetails.html",locals())
              
