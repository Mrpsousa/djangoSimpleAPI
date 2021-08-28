from django.test import TestCase
from rest_framework import status
from django.urls import reverse
from json import dumps


class ProductTest(TestCase):

    def setUp(self):
        self.valid_payload = {
            "name": "Cerveja Heineken",
            "category": "Bebida",
            "value": 9.99,
            "type": "Pilsen",
            "expiry_date": None,
            "quantity": 20,
            "inventory_alert": False,
            "set_date": "2021-12-30",
            "set_time": "02:02:02"
        }
    
    def test_create_valid_product(self):
        response = self.client.post(
            reverse('product'), 
            data=dumps(self.valid_payload), content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_list_all_product(self):
        response = self.client.get(reverse('product'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
