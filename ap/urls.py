from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.index,name="index"),
    path('singup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('home',views.home,name="home"),
    path('signout',views.signout,name="signout"),
    path('moviedetails<int:pk>',views.moviedetails,name='moviedetails'),
    path('play<int:pk>',views.play, name='play'),
    path('userdetails',views.userdetails,name="userdetails"),
    path('movielist',views.movielist,name="movielist"),
    path('normaluser',views.normaluser,name="normaluser"),
    path('language<slug:value>',views.language,name="language"),
    path('category<slug:value>',views.category,name="category"),
    path('del<slug:value>',views.delete,name="delete"),
    path('mdel<int:pk>',views.mdelete,name="mdelete"),
    path('update<slug:value>',views.update,name="update"),
    path('upuser<slug:value>',views.upuser,name="upuser"),
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
