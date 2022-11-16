from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template =  loader.get_template('index.html')
    return HttpResponse(template.render())


# Register method
def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())







# Create your views here.
