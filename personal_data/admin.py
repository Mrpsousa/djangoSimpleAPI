from django.contrib import admin
from .models import PersonalData


@admin.register(PersonalData)
class PersonalDataAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "value",
        "type",
        "expiry_date",
        "quantity",
        "inventory_alert",
        "set_date",
        "set_time",
        "created_at",
        "updated_at"
    )
