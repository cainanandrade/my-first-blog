""" 
Adicionando url's ao aplicativo blog

"""

from django.conf.urls import url
from . import views

#padrão url:

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
