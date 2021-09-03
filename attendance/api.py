from rest_framework.views import APIView
from attendance.services import create


class Atendimento(APIView):

    def post(self, request):
        return create(request.data)


