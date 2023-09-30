from django.shortcuts import render
from .models import Service  # Importa el modelo

def services(request):
   # Lista de servicios para acceder al modelo
   services = Service.objects.all()  # Utiliza "services.objects.all()"
   return render(request, "services/services.html", {'services': services})
