from django.db import models
from common.model_base import BaseModel


class Product(BaseModel):
    name = models.CharField('Nome', max_length=128)
    category = models.CharField('Categoria', max_length=128)
    value = models.FloatField('valor') 
    type = models.CharField('Tipo', max_length=32)
    expiry_date = models.DateField('Data de Validade', null=True, blank=True) #TODO: gerar automaticamente
    quantity = models.IntegerField('Quantidade')    
    inventory_alert = models.BooleanField('Alerta de Estoque') #TODO: verificar condição automaticamente
    set_date = models.DateField('Data de Marcação', null=True, blank=True)
    set_time = models.TimeField('Hora de Marcação', null=True, blank=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['id']
