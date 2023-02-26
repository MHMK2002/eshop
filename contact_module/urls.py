from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_us, name='contact-us'),
    path('submit-message', views.submit_message, name='submit-message'),
]