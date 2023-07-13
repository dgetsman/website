from typing import Any, Dict, Optional
from django.db import models
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import DetailView, FormView, TemplateView
from . import models, forms
from .models import Status
from directory.models import Books
from django.shortcuts import get_object_or_404


class CartDetailView(DetailView):
    template_name ="orders/cart.html"
    model = models.Cart

    def get_object(self, *args, **kwargs):
        pk = self.request.session.get("cart_id")
        customer = self.request.user
        if customer.is_anonymous:
            customer = None
        Cart, created = models.Cart.objects.get_or_create(
            pk=pk,
            defaults={
                "customer":customer
            }
        )
        good_id = self.request.GET.get("good_id")
        quantity = self.request.GET.get("quantity")
        if good_id and quantity:
            quantity=int(quantity)
            good = Books.objects.get(pk=int(good_id))
            price = good.price
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
        return Cart
    
class CartChangeView(DetailView):
    template_name ="orders/cart.html"
    model = models.Cart

    def get_object(self, *args, **kwargs):
        cart_pk = self.request.session.get("cart_id")
        customer = self.request.user
        if customer.is_anonymous:
            customer = None
        Cart, created = models.Cart.objects.get_or_create(
            pk=cart_pk,
            defaults={
                "customer":customer
            }
        )
        good_id = self.request.GET.get("good")
        action = self.request.GET.get("action")
        if good_id and action and action in ['add', 'delete']:
            good = Books.objects.get(pk=int(good_id))
            price = good.price
            good_in_cart = get_object_or_404(
                models.GoodInCart,
                cart__pk=Cart.pk,
                good__pk=good.pk
                )
            if action == 'add':
                addition = 1
            else:
                if good_in_cart.quantity == 1:
                    good_in_cart.delete()
                    return Cart
                addition = -1
            good_in_cart.quantity = good_in_cart.quantity + addition
            good_in_cart.price = good_in_cart.quantity * price
            good_in_cart.save()
        return Cart
    
class CreateOrder(FormView):
    form_class = forms.CreateOrderForm
    template_name = 'orders/create_order.html'
    success_url = reverse_lazy("orders:order-complete")

    def form_valid(self, form):
        delivery_address = form.cleaned_data.get("delivery_address")
        status = Status.objects.get(pk=1)
        cart_pk = int(self.request.session.get("cart_id"))
        cart = get_object_or_404(
            models.Cart,
            pk=cart_pk
        )
        obj = models.Order.objects.create(
            delivery_address=delivery_address,
            Status=status,
            Cart = cart
        )
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id = int(self.request.session.get("cart_id"))
        context["object"] = get_object_or_404(
            models.Cart,
            pk=cart_id
        )
        return context
    
class OrderComplete(TemplateView):
    template_name = "orders/order-complete.html"