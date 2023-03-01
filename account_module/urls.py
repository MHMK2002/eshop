from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegisterUser.as_view(), name='register-page'),
    path('login', views.LoginUser.as_view(), name='login-page')
]
