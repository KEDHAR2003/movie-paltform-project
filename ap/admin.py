from django.contrib import admin
from .models import Regestration,moviedatails

# Register your models here.
class RegestrationAdmin(admin.ModelAdmin):
    list_display = ['id','firstname','secondname','email','city']
    ordering = ['id']
admin.site.register(Regestration,RegestrationAdmin)

class moviedatailsAdmin(admin.ModelAdmin):
    list_display = ['id','title','language','category'] 
    ordering = ['id']
admin.site.register(moviedatails,moviedatailsAdmin)
