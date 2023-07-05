from typing import Any, Dict
from django.shortcuts import render
from random import randint
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy

from . import models
from . import forms


class HomePage(generic.TemplateView):
    template_name = "directory/home-page.html"

class BooksCreareView(generic.CreateView):
    template_name = 'directory/add-books.html'
    model = models.Books
    fields = [
        "Picture", "Genre", "name"
    ]
    success_url = "/directory/success"

class BooksUpdateView(generic.UpdateView):
    template_name = 'directory/add-books.html'
    model = models.Books
    fields = [
        "Genre", "name"
    ]
    success_url = "/directory/success"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message']='Edit the book'
        return context

class BooksDeleteView(generic.DeleteView):
    model = models.Books
    template_name = 'directory/delete-book.html'
    success_url = "/directory/list-view"

class BooksView(generic.DetailView):
    model = models.Books
    
class BooksListView(PermissionRequiredMixin, generic.ListView):
    login_url = reverse_lazy("manager:login")
    permission_required = [
        "directory.delete_Books",
        "directory.add_Books"
    ]
    model = models.Books
    template_name = 'directory/books-list-view.html'
    paginate_by = 10

def home_page(request):
    Books = models.Books.objects.filter(pk__lt=100)
    return render(request,
                   template_name='directory/home-page.html',
                   context={'objects':Books})

def success(request):
    return render(
    request,
        template_name="directory/success.html",
        context={"message":"Book was edited"}
    )

def send_gmail(request):
    if request.method == "GET":
        form = forms.ContactForm()
        return render(
            request,
            template_name="directory/send-gmail.html",
            context={"form":form}
        )
    else:
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/success")
        else:
            return render(
                request,
                template_name="directory/send-gmail.html",
            context={"form":form}
            )