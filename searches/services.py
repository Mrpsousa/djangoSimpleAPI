from rest_framework import status
from services.models import Service
from services.serializers import ServiceSerilizer
from rest_framework.response import Response


def createServices(data):
    search_ = dict
    services = []
    print(data)
    if data['city']:
        search_ = Service.objects.filter(city = data['city'])
    elif data['state']:
        search_ = Service.objects.filter(state = data['state'])
    elif data['category']:
        search_ = Service.objects.filter(category = data['category'])

    for data in search_:
        service = ServiceSerilizer(data).data
        services.append(service)
    return Response(services,
                    status=status.HTTP_200_OK) 


def createProducts(data):
    pass
