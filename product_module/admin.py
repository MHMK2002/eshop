from django.contrib import admin
from .models import Product, ProductCategory, ProductTag, ProductBrand


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductCategory)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductTag)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductBrand)
class ProductAdmin(admin.ModelAdmin):
    pass
