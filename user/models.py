from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from common.mixins.models import UdmModel
from rbac.models import UserRoleRelation, Role
from project.models import *
from project.serializers import *


# Create your models here.
class User(UdmModel, AbstractUser):
    full_name = models.CharField(max_length=16, verbose_name=_('姓名'))
    phone_number = models.CharField(max_length=16, blank=True, null=True, verbose_name=_('联系方式'))
    hospital_name = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('医院名称'))
    doctor_certificate = models.CharField(max_length=255, blank=True, null=True, verbose_name=_('执业医师资格证'))
    title = models.CharField(max_length=16, blank=True, null=True, verbose_name=_('职称'))

    @property
    def roles(self):
        """
        当前用户拥有的角色
        """
        relations = UserRoleRelation.objects.filter(user_id=self.id)
        role_id_list = [r.role_id for r in relations]
        return Role.objects.filter(id__in=role_id_list)

    @property
    def permissions(self):
        """
        当前用户拥有的权限
        """
        permissions = []
        for role in self.roles:
            permissions.append(role.permissions())
        return permissions

    def in_project(self, project_id: int):
        """
        用户是否在项目中
        @param project_id: 心脏、甲状腺等项目的 ID
        @return: True|False
        """
        try:
            pro = Project.objects.get(pk=project_id)
        except Project.DoesNotExist:
            return False
        else:
            return ProjectUserRelation.objects.filter(user_id=self.id, pro_id=pro.id).exists()

