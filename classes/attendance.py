from classes.database import DataBase


class Attendance(DataBase):

    def _init_(self):

        self.name: str = ""
        self.cpf: str = ""
        self.place: str = ""
        self.number: str = ""
        self.street: str = ""
        self.district: str = ""
        self.city: str = ""
        self.state: str = ""
        self.phone: str = ""
        self.product_name: str = ""
        self.product_category: str = ""
        self.product_value: float = 0.0
        self.product_type: str = ""
        self.service_name: str = ""
        self.service_category: str = ""
        self.service_date_time: str = ""
        self.service_value: float = 0.0

    def data_receive(self, data: dict) -> bool:

        self.name = data.get("name")
        self.cpf = data.get("cpf")
        self.place = data.get("place")
        self.number = data.get("number")
        self.street = data.get("street")
        self.district = data.get("district")
        self.city = data.get("city")
        self.state = data.get("state")
        self.phone = data.get("phone")
        self.product_name = data.get("product_name")
        self.product_category = data.get("product_category")
        self.product_value = data.get("product_value")
        self.product_type = data.get("product_type")
        self.service_name = data.get("service_name")
        self.service_category = data.get("service_category")
        self.service_value = data.get("service_value")

    def saveProducts2(self):

        data = {
            'name': self.product_name,
            'category': self.product_category,
            'value': self.product_value,
            'type': self.product_type,
        }

        self.saveProduct(data)

    def saveServices2(self):

        data = {
            'name': self.service_name,
            'category': self.service_category,
            'value': self.service_value,
        }

        self.saveService(data)
    
    def savePersonalData2(self):
        
        data = {
            'name': self.name,
            'cpf': self.cpf,
            'place': self.place,
            'number': self.number,
            'street': self.street,
            'district': self.district,
            'city': self.city,
            'state': self.state,
            'phone': self.phone
        }

        self.savePersonalData(data)
