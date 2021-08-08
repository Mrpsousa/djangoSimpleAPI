from django.shortcuts import render
from rest_framework import viewsets
from .searches import list_all

class Searches(viewsets.ModelViewSet):

    def list(self, request):
        return list_all()