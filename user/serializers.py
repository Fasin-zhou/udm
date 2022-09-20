# -*- coding: utf-8 -*-
"""
Author: xuqidong
Date: 2022/8/18 10:54
"""
from rest_framework import serializers

from .models import *


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project