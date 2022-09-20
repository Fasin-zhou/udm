from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.mixins.models import UdmModel, Status


# Create your models here.
class Project(UdmModel):
    project_name = models.CharField(max_length=32, unique=True, verbose_name=_('项目名称'))
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=1, verbose_name=_('状态'))
    desc = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('描述'))
    target = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('项目目标'))


class ProjectUserRelation(UdmModel):
    level_choices = (
        ('leader', '项目负责人'),
        ('member', '项目成员'),
    )
    pro_id = models.PositiveSmallIntegerField()
    user_id = models.PositiveSmallIntegerField()
    level = models.CharField(max_length=16, choices=level_choices, default='member', verbose_name=_('用户在项目中的级别'))
