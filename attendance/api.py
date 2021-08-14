from rest_framework.views import APIView
from classes.attendance import Attendance
from rest_framework import status
from rest_framework.response import Response
import json


att_: Attendance = Attendance()

class Atendimento(APIView):

    def post(self, request):
        #print(request.data)
        att_.data_receive(request.data)
        return Response(att_.__dict__ ,
                    status=status.HTTP_200_OK)


