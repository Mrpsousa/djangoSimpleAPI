from django.contrib import admin
from .models import Search


@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = ("service_search",
                    "city_search",
                    "category_search",
                    "state_search"
                    )
