# -*- coding: utf-8 -*-
"""
Author: xuqidong
Date: 2022/8/17 15:27
"""
class LogicError(Exception):
    """逻辑异常类"""
    code = 0

    def __str__(self):
        return self.__class__.__name__


def generate_logic_error(name, code, msg='ok'):
    """创建逻辑异常的子类"""
    base_cls = (LogicError,)
    return type(name, base_cls, {'code': code, 'msg': msg})


SUCCESS = generate_logic_error('SUCCESS', 0)
PARAM_NOT_VALID = generate_logic_error('PARAM_NOT_VALID', 100001, '参数非法')
PARAM_IS_NULL = generate_logic_error('PARAM_NOT_VALID', 100002, '参数为空')
USER_OR_PWD_ERROR = generate_logic_error('USER_OR_PWD_ERROR', 100003, '用户名或密码错误')
NOT_IN_PROJECT = generate_logic_error('USER_OR_PWD_ERROR', 100004, '用户不在项目中')