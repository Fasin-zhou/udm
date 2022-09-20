# -*- coding: utf-8 -*-
"""
Author: xuqidong
Date: 2022/7/26 9:51
"""
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UdmBaseModel(models.Model):
    """
    默认id的类型：BigAutoField
    """
    created_by = models.CharField(max_length=32, null=True, blank=True, verbose_name=_('Created by'))
    updated_by = models.CharField(max_length=32, null=True, blank=True, verbose_name=_('Updated by'))
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name=_('Date created'))
    date_updated = models.DateTimeField(auto_now=True, verbose_name=_('Date updated'))

    class Meta:
        abstract = True


class UdmModel(UdmBaseModel):
    id = models.AutoField(primary_key=True)

    class Meta:
        abstract = True


class Status(models.TextChoices):
    enable = 1, _('启用')
    disable = 0, _('禁用')
