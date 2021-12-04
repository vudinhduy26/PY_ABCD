# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 16:24:42 2021

@author: duy
"""

from django.urls import path,include
from . import views

app_name = "post"
urlpatterns = [
    path('',views.index,name="blog"),
    path('<int:id>/',views.postDetail,name='postDetail'),
]