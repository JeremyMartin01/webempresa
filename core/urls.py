
from django.contrib import admin
from django.urls import path
from core import views
urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("store/", views.store, name="store"),
    path("blog/", views.blog, name="Blog"),
    path("contact/", views.blog, name="Contacto"),
    path("sample/", views.sample, name="sample")
]