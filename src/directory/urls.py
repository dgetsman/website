from django.urls import path
from . import views
app_name = "directory"

urlpatterns = [
    path('dir/', views.home_page),
    path('books-view/<int:pk>', views.BooksView.as_view(),name = "books-view"),
    path('delete-books-view/<int:pk>', views.BooksDeleteView.as_view(),name="delete-books"),
    path('add-books-view/', views.BooksCreareView.as_view(),name="add-books"),
    path('update-books-view/<int:pk>', views.BooksUpdateView.as_view(),name="update-books"),
    path('success/', views.success,name="success"),
    path('list-view/', views.BooksListView.as_view(),name="list-view"),
    path('send-gmail/', views.send_gmail,name="send-gmail"),
]
