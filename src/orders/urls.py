from django.urls import path
from . import views

app_name = "orders"


urlpatterns = [
    path('cart/', views.CartDetailView.as_view(),name = "cart-view"),
    path('cart-edit/', views.CartChangeView.as_view(),name = "cart-edit-view"),
    path('create-order/', views.CreateOrder.as_view(),name = "create-order"),
    path('create-complete/', views.OrderComplete.as_view(),name = "order-complete"),
]