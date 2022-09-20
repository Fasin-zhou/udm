# -*- coding: utf-8 -*-
"""
Author: xuqidong
Date: 2022/8/18 15:16
"""
from .models import *
from common.api.utils import *
from project.domain import Menu



def login(user: User, project_id: int) -> APIV1BaseJsonResponse:
    if user.in_project(project_id):
        menu = []
        menu.append(Menu(1, "用户管理").to_dict())
        menu.append(Menu(2, "权限管理").to_dict())
        data = {"token": "ldslfsl", "menu": menu}
        return APIV1OKJsonResponse('登录成功', data=data)
    else:
        return APIV1FailJsonResponse(status_code.NOT_IN_PROJECT.msg, code=status_code.NOT_IN_PROJECT.code)