from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Service

class ServiceSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Service
        fields = "__all__"
