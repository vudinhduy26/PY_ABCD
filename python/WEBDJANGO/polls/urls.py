# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 07:19:36 2021

@author: duy
"""

from django.conf.urls import url 
 
from . import views 
 
urlpatterns = [ 
     url(r'^$', views.index, name='index'),
]