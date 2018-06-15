from django.urls import path
from . import views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect



urlpatterns = [
    path('', views.index, name = 'index'),
    path('index2', views.second, name = 'index2' ),
    path('form',views.sign,  name = 'form' ),
    path('login', views.user_login, name='user_login'),
    # path('favicon.ico', RedirectView.as_view(url='/static/images/favicon.ico')),
    path('favicon.ico', lambda x: HttpResponseRedirect(settings.STATIC_URL+'images/favicon.ico')),
]

# need to make some editingd to this file as changes had been made

#kelechi try o.. learn well so that you can tech me all you KNOW on DJANGO later................................s