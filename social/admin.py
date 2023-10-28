from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from . models import Link
# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    #Extender esto en tiempo de Ejecución
    
    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exists:
            return('created', 'updated', 'key', 'name')
        else:
            ('created', 'updated')

admin.site.register(Link, LinkAdmin)