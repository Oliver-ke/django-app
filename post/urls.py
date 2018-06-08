from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('index2', views.second, name = 'index2' ),
    path('form',views.sign,  name = 'form' ),
    path('login', views.user_login, name='user_login',
]


# need to make some editingd to this file as changes had been made