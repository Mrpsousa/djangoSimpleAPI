from classes.attendance import Attendance
from rest_framework import status
from rest_framework.response import Response


att_: Attendance = Attendance()


def create(data):
    att_.data_receive(data)

    return Response(att_.__dict__,
                       status=status.HTTP_201_CREATED)
               