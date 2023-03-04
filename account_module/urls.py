from django.urls import path
from . import views

urlpatterns = [
    path('register', views.RegisterUser.as_view(), name='register-page'),
    path('login', views.LoginUser.as_view(), name='login-page'),
    path('active-account/<str:email_activation_code>', views.ActivationUser.as_view()),
    path('forget-password', views.ForgotPassword.as_view(), name='forget-password'),
    path('reset-password/<str:password_activation_code>', views.ResetPassword.as_view(), name='reset-password'),
    path('logout', views.Logout.as_view(), name='logout')
]
