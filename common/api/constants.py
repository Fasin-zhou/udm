# -*- coding: utf-8 -*-
"""
Author: xuqidong
Date: 2022/7/26 18:58
"""


def enum(**enums):
    return type('Enum', (), enums)


ApiErrorCodeEnum = enum(
    SUCCESS='0',
    PARAM_NOT_VALID='10001',
    USER_NOT_EXISTS='10002',
)
