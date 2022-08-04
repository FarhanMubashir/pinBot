from django.contrib import admin
from django.urls import path,include

from .views import *
from pinBotApp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('apicall',views.apicall, name='apicall'),
    
    

]