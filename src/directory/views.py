from typing import Any, Dict
from django.shortcuts import render
from random import randint
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic

from . import models
from . import forms

class HomePage(generic.TemplateView):
    template_name = "directory/home-page.html"

class BooksCreareView(generic.CreateView):
    template_name = 'directory/add-books.html'
    model = models.Books
    fields = [
        "Genre", "name"
    ]
    success_url = "/edit-success"

class BooksUpdateView(generic.UpdateView):
    template_name = 'directory/add-books.html'
    model = models.Books
    fields = [
        "Genre", "name"
    ]
    success_url = "/edit-success"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message']='Edit the book'
        return context

class BooksDeleteView(generic.DeleteView):
    model = models.Books
    template_name = 'directory/delete-book.html'
    success_url = "/dir"

class BooksView(generic.DetailView):
    model = models.Books
    
class BooksListView(generic.ListView):
    model = models.Books
    template_name = 'directory/books-list-view.html'
    paginate_by = 10

def home_page(request):
    Books = models.Books.objects.filter(pk__lt=100)
    return render(request,
                   template_name='directory/home-page.html',
                   context={'objects':Books})

#def veiw_books(request, pk):
    Books = models.Books.objects.get(pk=int(pk))
    html = f"Books PK:{Books.pk} Books Name {Books.name}"
    return HttpResponse(html)

#def add_books(request):
    if request.method == "GET":
        form = forms.BooksModelForm()
        return render(
            request,
            template_name='directory/add-books.html',
            context={"greeting":"Add a new book", "form":form})
    else:
        books_form = forms.BooksModelForm(request.POST)
        if books_form.is_valid():
            new_book = books_form.save()
            return HttpResponseRedirect("/edit-success")
        else:
            return render(
            request,
            template_name='directory/add-books.html',
            context={"greeting":"Add a new book", "form":form}
            ) 

def success(request):
    return render(
    request,
        template_name="directory/success.html",
        context={"message":"Book was edited"}
    )

#def update_books(request, pk):
    if request.method == "GET":
        genre = models.Genre.objects.all()
        book = models.Books.objects.get(pk=pk)
        return render(
            request,
            template_name='directory/update-books.html',
            context={"object":book, "genres":genre, "greeting":"Edit the book"})
    else:
        book_name = request.POST.get("book_name")
        genre_id = request.POST.get("Genre")
        genre_all = models.Genre.objects.all
        genre = models.Genre.objects.get(pk=int(genre_id))
        new_book = models.Books.objects.update(name=book_name, Genre=genre)
        return render(request,
            template_name='directory/success.html',
            context={"genres":genre_all, "greeting":f"Book {book_name} was edited"}
        )