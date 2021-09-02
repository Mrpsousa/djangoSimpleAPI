from django.contrib import admin
from .models import PersonalData


@admin.register(PersonalData)
class PersonalDataAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "cpf",
        "place",
        "number",
        "street",
        "district",
        "city",
        "state",
        "phone"
    )
