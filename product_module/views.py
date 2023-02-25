from django.shortcuts import render
from .models import Product, ProductBrand, ProductCategory


# Create your views here.
def product_list(request):
    products = Product.objects.all()[:5]
    brands = ProductBrand.objects.all()
    categories = ProductCategory.objects.all()
    context = {
        'products': products,
        'brands': brands,
        'categories': categories
    }
    return render(request, 'product_module/product_list.html', context)


def product_box(request, slug):
    product = Product.objects.filter(slug=slug)[0]
    context = {
        'product': product,
    }
    return render(request, 'product_module/product_box.html', context)


def product_detail(request, slug):
    product = Product.objects.filter(slug=slug)[0]
    brands = ProductBrand.objects.all()
    categories = ProductCategory.objects.all()
    context = {
        'product': product,
        'brands': brands,
        'categories': categories
    }
    return render(request, 'product_module/product_detail.html', context)
