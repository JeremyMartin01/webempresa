from django.contrib import admin
from .models import Service
#Mostrar los campos 'created' y 'update' en modo 
# de solo lectura en el panel de administracion de Django. 

class servicesAdmin(admin.ModelAdmin):
    #list_display = ('title', 'subtitle', 'content', 'image', 'created', 'updated')
    readonly_fields = ('created', 'updated')
# Register your models here.

admin.site.register(Service, servicesAdmin)
