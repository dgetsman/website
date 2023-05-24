from django.shortcuts import render
from random import randint
from django.http import HttpResponse
from . import models

def home_page(request):
    genres = models.Genre.objects.filter(pk__lt=10)
    return render(request,
                   template_name='genrehomepage/home-page.html',
                   context={'objects':genres})

def veiw_genre(request, pk):
    genre = models.Genre.objects.get(pk=int(pk))
    html = f"Genre PK:{genre.pk} Genre Name {genre.name}"
    return HttpResponse(html)
