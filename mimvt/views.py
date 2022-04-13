from contextvars import Context
from django.shortcuts import render

from django.forms import CharField
from django.http import HttpResponse
from django.template import Template
from django.template import Context

from .models import familiares, profesiones


def saluda(request):
    mihtml=open("C:/Users/Carucha/Desktop/mi primer MVT Monserrat/ProyectoMVT/mimvt/Templates.html")
    plantilla=Template(mihtml.read())
    mihtml.close()
    micontexto=Context()
    return HttpResponse(plantilla.render(micontexto))



def familiar(request,nombre,apellido,dni):
    mis_nombre= familiares(nombre=nombre,apellido=apellido,dni=dni)
    mis_nombre.save()
    
    return HttpResponse(f'Hola mi familiar es {mis_nombre.nombre} {mis_nombre.apellido} y su dni es: {mis_nombre.dni} ')

def profesion(request,profesion):
    mi_profesion= profesiones(profesion=profesion)
    mi_profesion.save()
    
    return HttpResponse(f'Su profesion es {mi_profesion.profesion}')



    
    