from django.urls import path
from .api import Atendimento


urlpatterns = [
    path('attendance/', Atendimento.as_view(),
         name='atendimento'),
    
]
