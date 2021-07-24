from rest_framework import viewsets
from .models import Service
from .serializers import ServiceSerilizer
from .services import create, list_all


class Services(viewsets.ModelViewSet):

    def create(self, request):
       return create(request.data)


    def list(self, request):
      return list_all()

