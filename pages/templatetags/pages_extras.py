from django import template
from pages.models import Page

#Transformamos una función normal, en un simple_tag y lo registramos en la libreria de templates.

#Hay que detener y reinicial el server para que guarde el cambio en memoria.
register = template.Library()

@register.simple_tag
def get_page_list():
    pages = Page.objects.all()
    return pages