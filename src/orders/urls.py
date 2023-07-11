from django.urls import path
from . import views

app_name = "orders"


urlpatterns = [
    path('cart/', views.CartDetailView.as_view(),name = "cart-view")
]