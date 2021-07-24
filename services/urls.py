from django.conf.urls import url
from .api import Services

list_actions = {
    'get': 'list',
    'post': 'create'
}


urlpatterns = [
    url('service/', Services.as_view(list_actions),
        name='service')
]