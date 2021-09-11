from .models import PersonalData
from .serializers import PersonalDataSerializer
from rest_framework import status
from rest_framework.response import Response


def create(data):
    personaldata = PersonalData.objects.create(
                                            name=data['name'],
                                            cpf=data['cpf'],
                                            place=data['place'],
                                            number=data['number'],
                                            street=data['street'],
                                            district=data['district'],
                                            city=data['city'],
                                            state=data['state'],
                                            phone=data['phone']
                                            )
    return Response(PersonalDataSerializer(personaldata).data,
                    status=status.HTTP_201_CREATED)


def list_all():
    personalDatas = []

    datas = PersonalData.objects.filter()

    for data in datas:
        personalData = PersonalDataSerializer(data).data
        personalDatas.append(personalData)

    return Response(personalDatas,
                    status=status.HTTP_200_OK)
