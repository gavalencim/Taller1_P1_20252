from django.shortcuts import render
from django.http import HttpResponse # Clase usada para construir respuestas HTTP en django

# Create your views here.
def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    #return render(request, 'home.html') # Plantilla sin parámetros
    return render(request, 'home.html', {'name':'Greg Lim'})

