from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.response import Response
from datetime import date, timedelta


def create(data):
    product = Product.objects.create(
                                name=data['name'],
                                category=data['category'],
                                value=data['value'],
                                type=data['type'],
                                expiry_date=(date.today() + timedelta(days=30)),
                                quantity=data['quantity'],
                                inventory_alert=(True if data['quantity'] < 10 else False),
                                set_date=data['set_date'],
                                set_time=data['set_time']
                                )
    return Response(ProductSerializer(product).data,
                    status=status.HTTP_201_CREATED)


def list_all():
    products = []

    datas = Product.objects.filter()

    for data in datas:
        product = ProductSerializer(data).data
        products.append(product)

    return Response(products,
                    status=status.HTTP_200_OK)
