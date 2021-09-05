
class Attendance():

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

    # TODO: TUDO EM INGLÊS
    # TODO: criar outro app pra gerir o atendimento (não tem serializer nem model)
    # Nome pessoa: name
    # cpf pessoa : cpf
    # logradouro: place
    # número: number
    # rua: street
    # bairro: (block?)
    # cidade: city
    # estado: state
    # telefone: phone
    # produto: product
    # quantidade de produto: product_quantity
    # nome serviço: service_name
    # data / horas de agendamento do serviço: date_time
    # valor do serviço: service_price
    # valor do produto por unidade: product_unit_price

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
       self.product = data.get("product")
       self.service_name = data.get("service_name")
       self.product_quantity = data.get("product_quantity")
       self.service_date_time = data.get("service_date_time")
       self.service_price = data.get("service_price")
       self.product_unit_price = data.get("product_unit_price")

        # self.name = data["name"]

        
