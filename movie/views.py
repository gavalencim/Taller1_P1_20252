from django.shortcuts import render
from django.http import HttpResponse # Clase usada para construir respuestas HTTP en django

from .models import Movie
# Create your views here.
def home(request):
    #return HttpResponse('<h1>Welcome to Home Page</h1>')
    #return render(request, 'home.html') # Plantilla sin parámetros
    #return render(request, 'home.html', {'name':'Ginna Alejandra'})
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Movie.objects.filter(title__icontains=searchTerm)
    else:
        movies = Movie.objects.all()
    return render(request, 'home.html', {'searchTerms':searchTerm, 'movies':movies, 'name':'Ginna Alejandra'})

def about(request):
    return render(request, 'about.html')

