# -*- coding: utf-8 -*-
"""
Author: xuqidong
Date: 2022/8/18 16:30
"""
from django.urls import path

from project import views

urlpatterns = [
    path('projects', views.ProjectMgr.as_view({'get':'list_project'}))
]