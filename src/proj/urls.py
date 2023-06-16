"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from directory import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dir/', views.home_page),
    path('books-view/<int:pk>', views.BooksView.as_view(),name = "books-view"),
    path('delete-books-view/<int:pk>', views.BooksDeleteView.as_view(),name="delete-view"),
    path('add-books-view/', views.BooksCreareView.as_view(),name="add-books"),
    path('update-books-view/<int:pk>', views.BooksUpdateView.as_view(),name="update-books"),
    path('edit-success/', views.success,name="success"),
    path('',views.HomePage.as_view(),name="home-page"),
    path('list-view/', views.BooksListView.as_view(),name="list-view"),
    path('send-gmail/', views.send_gmail,name="send-gmail"),

]
