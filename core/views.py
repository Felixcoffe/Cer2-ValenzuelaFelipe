from django.shortcuts import render, HttpResponse
from core.models import Correspondencia
from django.db.models import Q

# Create your views here.

def home(request):
    return render(request,'core/home.html')

def paquetes(request):
    return render(request, 'core/paquetes.html')

def buscar(request):
    if request.GET["correo"]:
        mensaje= "Correo Buscado %r" %request.GET["correo"]
        correo1= request.GET["correo"]
    
        x= Correspondencia.objects.filter(Destino__icontains=correo1)
        return render(request,"core/home.html",{"Correspondencias":x, "query":correo1})
    else: 
        mensaje = "Error"    
    return HttpResponse(mensaje)