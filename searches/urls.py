from django.urls import path
from .api import SearchProducts, SearchService


urlpatterns = [
    path('search/', SearchService.as_view(),
         name='searchservice'),
    path('searchproduct/', SearchProducts.as_view(),
         name='searchproduct')
]
