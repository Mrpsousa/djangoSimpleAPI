from rest_framework import status
from services.models import Service
from products.models import Product
from services.serializers import ServiceSerilizer
from products.serializers import ProductSerializer
from rest_framework.response import Response


def createServices(data):
    search_ = dict
    services = []
 
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
    product_ = dict
    productes = []
   
    if data['type']:
        product_ = Product.objects.filter(type = data['type'])
    elif data['category']:
        product_ = Product.objects.filter(category = data['category'])

    for data in product_:
            product = ProductSerializer(data).data
            productes.append(product)
    return Response(productes,
                        status=status.HTTP_200_OK) 
