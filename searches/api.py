from rest_framework.views import APIView
from .services import createServices, createProducts

class SearchService(APIView):

    def post(self, request):
        return createServices(request.data)

class SearchProducts(APIView):

    def post(self, request):
        return createProducts(request.data)