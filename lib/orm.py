# -*- coding: utf-8 -*-
"""
Author: xuqidong
Date: 2022/8/18 14:46
"""
class ModelMixin:
    def to_dict(self, ignore_fields=()):
        '''将model对象转换成dict'''
        data = {}
        for field in self._meta.fields:
            name = field.attname
            if name not in ignore_fields:
                data[name] = getattr(self, name)
        return data