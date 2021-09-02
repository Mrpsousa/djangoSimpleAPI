from django.db import models
from common.model_base import BaseModel
# Create your models here.


class PersonalData(BaseModel):
    name = models.CharField('Nome', max_length=128)
    cpf = models.CharField('CPF', max_length=16)
    place = models.CharField('Endereço', max_length=255)
    number = models.CharField('Número', max_length=6)
    street = models.CharField('Rua', max_length=255)
    district = models.CharField('Bairro', max_length=64)
    city = models.CharField('Cidade', max_length=64)
    state = models.CharField('Estado', max_length=64)
    phone = models.CharField('Telefone', max_length=16)

    class Meta:
        verbose_name = 'Dados Pessoais'
        verbose_name_plural = 'Dados Pessoais'
        ordering = ['id']
