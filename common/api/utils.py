# -*- coding: utf-8 -*-
"""
Author: xuqidong
Date: 2022/7/26 19:09
"""
from django.http import JsonResponse
from rest_framework.response import Response
from common.api.constants import ApiErrorCodeEnum
from rest_framework.views import exception_handler

from . import status_code

class ApiResponse(Response):
    def __init__(self, success=True, errorCode=100, errorMessage='success', data=[], status=None, template_name=None, headers=None, exception=False, content_type=None, **kwargs):
        if not success:
            errorMessage='fail'
            errorCode=400
        dic = {
            "success":success,
            "errorCode":errorCode,
            "errorMessage":errorMessage,
            "data":data,
        }
        if data:
            dic['data'] = data
        if kwargs:
            dic.update(kwargs)
        super().__init__(data=dic, status=status, template_name=template_name, headers=headers, exception=exception, content_type=content_type)

class ApiErrorResponse(Response):
    def __init__(self, success=False, errorCode=500, errorMessage='fail', data=[], status=None, template_name=None, headers=None, exception=False, content_type=None, **kwargs):
        dic = {
            "success":success,
            "errorCode":errorCode,
            "errorMessage":errorMessage,
            "data":data,
        }
        if data:
            dic['data'] = data
        if kwargs:
            dic.update(kwargs)
        super().__init__(data=dic, status=status, template_name=template_name, headers=headers, exception=exception, content_type=content_type)


def login_exception_handler(exc,context):
    response = exception_handler(exc,context)
    if response is not None:
        detail = response.data
        response.data={}
        response.data['success'] = False
        response.data['errorCode'] = response.status_code
        response.data['errorMessage'] = detail
    return response

class APIV1BaseJsonResponse(JsonResponse):
    def __init__(self, result, code, message, data=None):
        data = data if data is not None else {}
        json_data = {'success': result, 'data': data, 'errorCode': code, 'errorMessage': message}
        super(APIV1BaseJsonResponse, self).__init__(json_data)


class APIV1FailJsonResponse(APIV1BaseJsonResponse):
    def __init__(self, message, **kwargs):
        code = kwargs.get('code') or status_code.PARAM_NOT_VALID.code
        data = kwargs.get('data')
        super(APIV1FailJsonResponse, self).__init__(False, code, message, data=data)


class APIV1OKJsonResponse(APIV1BaseJsonResponse):
    def __init__(self, message=None, **kwargs):
        data = kwargs.get("data")
        super(APIV1OKJsonResponse, self).__init__(True, status_code.SUCCESS.code, message, data=data)


def is_none(*args):
    none_values = ['', '0']
    for i in args:
        if i in none_values:
            return True
    return False
