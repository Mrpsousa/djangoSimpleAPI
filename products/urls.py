from django.conf.urls import url
from .api import Products


list_actions = {
    'get': 'list',
    'post': 'create'
}

urlpatterns = [
    url('product/', Products.as_view(list_actions), name='product')
]
