from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from json import dumps
# Create your tests here.


class ServiceTest(TestCase):
   
    def setUp(self):
        self.valid_payload = {
                        "name":"Manicure Maria",
                        "category":"Beleza",
                        "description":"Cuido das suas unhas",
                        "city":"Salvador",
                        "state":"Bahia",
                        "phone":"071 991230764",
                        "value": 20.00,
                        "set_date": "2021-01-18",
                        "set_time": "02:02:02" }

    def test_create_valid_service(self):
        response = self.client.post(reverse('service'), data=dumps(self.valid_payload),
                                    content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_list_all_service(self):
        response = self.client.get(reverse('service'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)