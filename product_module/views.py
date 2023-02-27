from django.shortcuts import render
from .models import Product, ProductBrand, ProductCategory
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView


# Create your views here.

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    brands = ProductBrand.objects.all()
    categories = ProductCategory.objects.all()
    extra_context = {
        'brands': brands,
        'categories': categories
    }
    template_name = 'product_module/product_list.html'


class ProductBoxView(TemplateView):
    template_name = 'product_module/product_box.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['slug'] = kwargs['slug']
        return context


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['brands'] = ProductBrand.objects.all()
        context['categories'] = ProductCategory.objects.all()
        return context


