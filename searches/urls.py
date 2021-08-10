from django.urls import path
from .api import SearchService


urlpatterns = [
    path('search/', SearchService.as_view(),
         name='searchService')
]
