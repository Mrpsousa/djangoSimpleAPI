from django.db import models
from common.model_base import BaseModel


class Product(BaseModel):
    name = models.CharField('Nome', max_length=128)
    category = models.CharField('Categoria', max_length=128)
    value = models.FloatField('valor') 
    type = models.CharField('Tipo', max_length=32)
    expiry_date = models.DateField('Data de Validade')
    quantity = models.IntegerField('Quantidade')    
    inventory_alert = models.BooleanField('Alerta de Estoque')
    set_date = models.DateField('Data de Marcação', auto_now=True)
    set_time = models.TimeField('Hora de Marcação', auto_now=True)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['id']
