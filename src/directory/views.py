from django.shortcuts import render
from random import randint
from django.http import HttpResponse
from . import models

def home_page(request):
    Books = models.Books.objects.filter(pk__lt=10)
    return render(request,
                   template_name='view-html/home-page.html',
                   context={'objects':Books})

def veiw_books(request, pk):
    Books = models.Books.objects.get(pk=int(pk))
    html = f"Books PK:{Books.pk} Books Name {Books.name}"
    return HttpResponse(html)

def add_books(request):
    return render(
        request,
        template_name='view-html/add-books.html',
        context={}
)