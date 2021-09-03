from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from json import dumps



class SearchService(TestCase):

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
        response = self.client.post(reverse('searchservice'), data=dumps(self.valid_payload),
                                    content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)



class SearchProduct(TestCase):

    def setUp(self):
        self.valid_payload = {
            "name": "Cerveja Heineken",
            "category": "Bebida",
            "value": 9.99,
            "type": "Pilsen",
            "expiry_date": "2022-01-30",
            "quantity": 20,
            "inventory_alert": False,
            "set_date": "2021-12-30",
            "set_time": "02:02:02"
        }

    def test_create_valid_product(self):
        response = self.client.post(
            reverse('searchproduct'), 
            data=dumps(self.valid_payload), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)        