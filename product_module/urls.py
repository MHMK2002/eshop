from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<slug:slug>', views.product_box, name='product'),
    path('product-details/<slug:slug>', views.product_detail, name='product_detail')
]