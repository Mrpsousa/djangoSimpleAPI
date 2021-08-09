from django.contrib import admin
from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name",
                    "category",
                    "description",
                    "city",
                    "state",
                    "phone",
                    "value",
                    "set_date",
                    "set_time")
