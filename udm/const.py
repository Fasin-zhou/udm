# -*- coding: utf-8 -*-
"""
Author: xuqidong
Date: 2022/7/28 10:26
"""
import os

from .conf import ConfigManager

__all__ = ['BASE_DIR', 'PROJECT_DIR', 'VERSION', 'CONFIG']

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PROJECT_DIR = os.path.dirname(BASE_DIR)
PROJECT_DIR = BASE_DIR
VERSION = '1.0.0'
CONFIG = ConfigManager.load_user_config()