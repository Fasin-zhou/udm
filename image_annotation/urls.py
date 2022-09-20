# -*- coding: utf-8 -*-
"""
Author: xuqidong
Date: 2022/8/2 13:22
"""
from django.urls import path

from image_annotation import views

urlpatterns = [
    path('img/', views.Image.as_view())
]