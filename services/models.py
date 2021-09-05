from django.db import models
from common.model_base import BaseModel


class Service(BaseModel):
    name = models.CharField('Nome', max_length=128)
    category = models.CharField('Categoria', max_length=128)
    description = models.TextField('Descrição', null=True, blank=True)
    city = models.CharField('Cidade', max_length=64, null=True, blank=True)  
    state = models.CharField('Estado', max_length=64, null=True, blank=True)    
    phone = models.CharField('Telefone', max_length=16, null=True, blank=True)
    value = models.FloatField('valor')
    set_date = models.DateField('Data de Marcação', null=True, blank=True)
    set_time = models.TimeField('Hora de Marcação', null=True, blank=True)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['id']
