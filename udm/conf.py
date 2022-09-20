# -*- coding: utf-8 -*-
"""
Author: xuqidong
Date: 2022/7/28 10:27
"""
import os
import sys
from importlib import import_module

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PROJECT_DIR = os.path.dirname(BASE_DIR)
PROJECT_DIR = BASE_DIR


def import_string(dotted_path):
    try:
        module_path, class_name = dotted_path.rsplit('.', 1)
    except ValueError as err:
        raise ImportError("%s doesn't look like a module path" % dotted_path) from err

    module = import_module(module_path)

    try:
        return getattr(module, class_name)
    except AttributeError as err:
        raise ImportError('Module "%s" does not define a "%s" attribute/class' % (
            module_path, class_name)
                          ) from err


class Config(dict):
    """
    配置分类：
    1. Django使用的配置文件，写到settings中
    2. 程序需要, 用户不需要更改的写到settings中
    3. 程序需要, 用户需要更改的写到config中
    """
    defaults = {
        'DEBUG': False,
        'DEBUG_DEV': False,
        'LOG_LEVEL': 'DEBUG',
        'LOG_DIR': os.path.join(PROJECT_DIR, 'logs'),
        'DB_ENGINE': 'mysql',
        'DB_NAME': 'test',
        'DB_HOST': 'localhost',
        'DB_PORT': 3306,
        'DB_USER': 'root',
        'DB_PASSWORD': 'root1234',
        'REDIS_HOST': 'localhost',
        'REDIS_PORT': 6379,
        'REDIS_PASSWORD': '',
        'REDIS_USE_SSL': False,

        'HTTP_LISTEN_PORT': 8080,
        'LANGUAGE_CODE': 'zh-hans',
        'TIME_ZONE': 'Asia/Shanghai',
    }

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, dict.__repr__(self))

    def get_from_config(self, item):
        try:
            value = super().__getitem__(item)
        except KeyError:
            value = None
        return value

    def get_from_env(self, item):
        value = os.environ.get(item, None)
        if value is not None:
            value = self.convert_type(item, value)
        return value

    def get(self, item):
        # 再从配置文件中获取
        value = self.get_from_config(item)
        if value is not None:
            return value
        # 其次从环境变量来
        value = self.get_from_env(item)
        if value is not None:
            return value
        value = self.defaults.get(item)
        return value

    def __getitem__(self, item):
        return self.get(item)

    def __getattr__(self, item):
        return self.get(item)


class ConfigManager:
    config_class = Config

    def __init__(self, root_path=None):
        self.root_path = root_path
        self.config = self.config_class()

    def from_object(self, obj):
        """
        @param obj: an import name or object
        """
        if isinstance(obj, str):
            obj = import_string(obj)
        for key in dir(obj):
            if key.isupper():
                self.config[key] = getattr(obj, key)

    def load_from_object(self):
        sys.path.insert(0, PROJECT_DIR)
        try:
            # from config import config as c
            # self.from_object(c)
            return True
        except ImportError:
            pass
        return False

    @classmethod
    def load_user_config(cls, root_path=None, config_class=None):
        config_class = config_class or Config
        cls.config_class = config_class
        if not root_path:
            root_path = PROJECT_DIR

        manager = cls(root_path=root_path)
        if manager.load_from_object():
            config = manager.config
        else:
            msg = """

                    Error: No config file found.

                    You can run `cp config_example.yml config.yml`, and edit it.
                    """
            raise ImportError(msg)

        return config
