# -*- coding: utf-8 -*-
"""
Author: xuqidong
Date: 2022/8/17 15:56
"""
from django.urls import path

from user import views

urlpatterns = [
    path('login', views.Login.as_view())
]