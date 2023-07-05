from django.shortcuts import render
from django.contrib.auth import views as auth_view

class LoginView(auth_view.LoginView):
    template_name = 'manager/login.html'

class LogoutView(auth_view.LogoutView):
    template_name = 'manager/logout.html'