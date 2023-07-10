from django.shortcuts import render
from django.views.generic import DetailView
from . import models

class CartDetailView(DetailView):
    template_name ="orders/cart.html"
    model = models.Cart

