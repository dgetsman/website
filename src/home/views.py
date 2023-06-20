from django.shortcuts import render
from django.views import generic
# Create your views here.

class HomePage(generic.TemplateView):
    template_name = "home/home-page.html"


    #python -m pip install Pillow
    #python.exe -m pip intstall
    #pip freeze > req.txt