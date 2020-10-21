from django.urls import path

from . import views

urlpatterns = [
    path('login',views.login,name = 'login'),
    path('register',views.register,name = 'register'),
    path('logout',views.register,name = 'logout'),
    path('dashboard',views.register,name = 'dashboard'),
]