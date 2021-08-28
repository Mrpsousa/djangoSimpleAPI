from .models import Service
from .serializers import ServiceSerilizer
from rest_framework import status
from rest_framework.response import Response


def create(data):
    service = Service.objects.create(
                                name=data['name'],
                                category=data['category'],
                                description=data['description'],
                                city=data['city'],
                                state=data['state'],
                                phone=data['phone'],
                                value=data['value'],
                                set_date=data['set_date'],
                                set_time=data['set_time']
                                )
    return Response(ServiceSerilizer(service).data,
                    status=status.HTTP_201_CREATED)


def list_all():
    services = []

    datas = Service.objects.filter()

    for data in datas:
        service = ServiceSerilizer(data).data
        services.append(service)
    return Response(services,
                    status=status.HTTP_200_OK)
