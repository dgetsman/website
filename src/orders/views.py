from typing import Any, Optional
from django.db import models
from django.shortcuts import render
from django.views.generic import DetailView
from . import models
from directory.models import Books


class CartDetailView(DetailView):
    template_name ="orders/cart.html"
    model = models.Cart

    def get_object(self, *args, **kwargs):
        pk = self.request.session.get("cart_id")
        customer = self.request.user
        Cart, created = models.Cart.objects.get_or_create(
            pk=pk,
            defaults={
                "customer":customer
            }
        )
        good_id = int(self.request.GET.get("good_id"))
        good = models.Books.objects.get(pk=good_id)
        quantity = int(self.request.GET.get("quantity"))
        price = models.Books.price()
        good_in_cart, good_created = models.GoodInCart.objects.get_or_create(
            cart=Cart,
            good=good,
            defaults={
                "quantity":quantity,
                "price":price * quantity
            },
            #quantity=quantity,
            #price=price
        )
        if not good_created:
            good_in_cart.quantity = good_in_cart.quantity + quantity
            good_in_cart.price = good_in_cart.price + price * quantity
            good_in_cart.save()
        if created:
            self.request.session['cart_id'] = Cart.pk
        return {}