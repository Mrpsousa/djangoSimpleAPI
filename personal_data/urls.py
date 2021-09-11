from django.conf.urls import url
from .api import PersonalDatas


list_actions = {
    'get': 'list',
    'post': 'create'
}

urlpatterns = [
    url('personaldata/', PersonalDatas.as_view(list_actions),
        name='personaldata')
]
