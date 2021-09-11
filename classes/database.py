from products.models import Product
from services.models import Service
from personal_data.models import PersonalData


class DataBase:
    @staticmethod
    def saveProduct(data):
        try:
            # print("saveProduct: ", data)
            Product.objects.create(
                                name=data['name'],
                                category=data['category'],
                                value=data['value'],
                                type=data['type']
                                )

        except Exception as e:
            print("Error saveProduct:", e)

    @staticmethod
    def saveService(data):
        try:
            # print("saveService", data)
            Service.objects.create(
                                name=data['name'],
                                category=data['category'],
                                value=data['value'],
                                set_date=data['set_date'],
                                set_time=data['set_time']
                                )

        except Exception as e:
            print("Error saveService:", e)
    
    @staticmethod
    def savePersonalData(data):
        try:
            # print("savePersonalData", data)
            PersonalData.objects.create(
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

        except Exception as e:
            print("Error savePersonalData:", e)
