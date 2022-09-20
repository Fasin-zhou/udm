# -*- coding: utf-8 -*-
"""
Author: xuqidong
Date: 2022/8/18 13:09
"""
class Menu:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }