from .models import PersonalData
from .serializers import PersonalDataSerializer
from rest_framework import status
from rest_framework.response import Response


def create(data):
    PersonalData = PersonalData.objects.create(
                                            name=data['name'],
                                            cpf=data['cpf'],
                                            place=data['place'],
                                            number=data['number'],
                                            street=data['street'],
                                            district=data['district'],
                                            city=data['city'],
                                            state=data['state'],
                                            phone=data['phone'],
                                            set_date=data['set_date'],
                                            set_time=data['set_time']
                                            )
    return Response(PersonalDataSerializer(PersonalData).data,
                    status=status.HTTP_201_CREATED)


def list_all():
    PersonalDatas = []

    datas = PersonalData.objects.filter()

    for data in datas:
        PersonalData = PersonalDataSerializer(data).data
        PersonalDatas.append(PersonalData)

    return Response(PersonalDatas,
                    status=status.HTTP_200_OK)
