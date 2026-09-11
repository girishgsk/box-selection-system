from django.contrib import admin

from .models import Product, Box


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "length",
        "width",
        "height",
        "weight",
    )


@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "length",
        "width",
        "height",
        "max_weight",
        "cost",
    )