from django.http import HttpResponse
from  django.template import loader
from django.shortcuts import render

from .models import Prueba

# Create your views here.
def index(request):
    alumno_uno = Prueba(nombre="Emiliano")
    alumno_dos = Prueba(nombre="Mario")
    alumno_tres = Prueba(nombre="Javier")
    alumno_uno.save()
    alumno_dos.save()
    alumno_tres.save()
    
    # template= loader.get_template('index.html')
    # render =  template.render({'lista_objetos':[alumno_uno,alumno_dos,alumno_tres]})
    # return HttpResponse(render)
    return render(request, 'index.html',{'lista_objetos':[alumno_uno,alumno_dos,alumno_tres]})