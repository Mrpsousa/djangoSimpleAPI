from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "value",
        "type",
        "expiry_date",
        "quantity",
        "inventory_alert",
        "set_date",
        "set_time"
    )
