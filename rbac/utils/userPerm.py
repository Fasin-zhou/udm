# -*- coding: utf-8 -*-
"""
Author: xuqidong
Date: 2022/8/1 13:52
"""
from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    message = '权限不足'
    def has_permission(self, request, view):
        perm_urls = []
        # return False
        for perm in request.user.permissions:
            perm_urls.append(perm.url)
        if request.path in perm_urls:
            # 请求的url在权限url列表中，有权限；否则无权限
            return True
        else:
            return False


