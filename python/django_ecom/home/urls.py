# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 16:06:23 2021

@author: duy
"""

from django.urls import path,include
from . import views

app_name = 'home'
urlpatterns = [
    path('',views.index, name='home'),
]