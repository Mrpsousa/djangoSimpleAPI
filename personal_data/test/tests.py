from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from json import dumps


class PersonalDataTest(TestCase):

    def setUp(self):
        self.valid_payload = {
            "name": "Claudia",
            "cpf": "06258745872",
            "place": "rua das araras",
            "number": "261",
            "street": "rua das araras",
            "district": "imbui",
            "city": "salvador",
            "state": "bahia",
            "phone": "71998755448"
        }
    
    def test_create_valid_personaldata(self):
        response = self.client.post(
            reverse('personaldata'),
            data=dumps(self.valid_payload), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_list_all_personaldata(self):
        response = self.client.get(reverse('personaldata'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
