from django.conf.urls import url
from .api import Searches

list_actions = {
    'get': 'list'
}


urlpatterns = [
    url('searches', Searches.as_view(list_actions),
        name='searches')
]
