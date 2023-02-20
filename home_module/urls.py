from django.urls import path
from . import views

urlpatterns = [
    path('', views.reverse_home),
    path('home', views.home, name='home')
]