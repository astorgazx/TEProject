from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import *
from django.views.decorators.csrf import *

def index(request):
    template =  loader.get_template('index.html')
    return HttpResponse(template.render())


# Register method
@csrf_protect
def register(request):
    
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Alumno registrado correctamente")
        else:
            return HttpResponse("Error al registrar alumno")
    return render(request, 'register.html', {'form': AlumnoForm()})

@csrf_protect

def registerTramite(request):
    if request.method == 'POST':
        form = TramiteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Tramite registrado correctamente")
        else:
            return HttpResponse("Error al registrar tramite")
    return render(request, 'registroTramite.html', {'form': TramiteForm()})








# Create your views here.
