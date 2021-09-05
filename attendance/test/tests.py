from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from json import dumps


class AttendanceTest(TestCase):

    def setUp(self):
        self.valid_payload = {
        "name":"Pedro",
        "cpf": "123456789",
        "place": "D",
        "number":"19",
        "street": "rua do rio",
        "district":"Centro",
        "city": "Salvador",
        "state":"BA",
        "phone": "73-000000000",
        "product_name": "arroz",
        "product_category":"limentício",
        "product_value": 4.0,
        "product_type":"tipo1",
        "service_name":"comida",  
        "service_category":"categoria01", 
        "service_value": 12.00,
        "set_date":"2021-01-18",
        "set_time":"02:02:02"
        }
    
    def test_create_valid_attendance(self):
        response = self.client.post(
            reverse('attendance'), 
            data=dumps(self.valid_payload), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    

