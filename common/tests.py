# -*- coding: utf-8 -*-
"""
Author: xuqidong
Date: 2022/8/18 18:23
"""
import os

from django.test import TestCase
from .api.utils import *

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "udm.settings")


class UtilTest(TestCase):
    def setUp(self) -> None:
        pass

    def test_is_none(self):
        res = is_none('abc','',0)
        self.assertTrue(res)