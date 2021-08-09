from django.urls import path
from .api import SearchService



urlpatterns = [
    path('searchService/', SearchService.as_view(),
        name='searchService')
]
