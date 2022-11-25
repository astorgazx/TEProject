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


def showTramites(request):
    if request.method == 'GET':
        tramites = Tramites.objects.all()
        return render(request, 'showTramites.html', {'tramites': tramites})

@csrf_protect
def editTramite(request, id):
    if request.method == 'GET':
        tramite = Tramites.objects.get(claveTramite=id)
        return render(request, 'editTramite.html', {'tramite': tramite})
    if request.method == 'POST':
        tramite = Tramites.objects.get(claveTramite=id)
        form = TramiteForm(request.POST, instance=tramite)
        if form.is_valid():
            form.save()
            return HttpResponse("Tramite actualizado correctamente")
        else:
            return HttpResponse("Error al actualizar tramite")

@csrf_protect
def delTramite(request, id):
    if request.method == 'GET':
        tramite = Tramites.objects.get(claveTramite=id)
        tramite.delete()
        return HttpResponse("Tramite eliminado correctamente")





# Create your views here.
