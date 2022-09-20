from django.db import models
from django.utils.translation import ugettext_lazy as _

from common.mixins.models import UdmModel, Status


class Role(UdmModel):
    name = models.CharField(max_length=16, unique=True, verbose_name=_("角色名称"))
    level = models.PositiveSmallIntegerField(unique=True, verbose_name=_("角色等级"))
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=1, verbose_name=_('状态'))
    desc = models.CharField(max_length=256, blank=True, null=True, verbose_name=_("描述"))

    def permissions(self):
        """
        当前角色拥有的权限
        """
        relations = RolePermissionRelation.objects.filter(role_id=self.id)
        perm_id_list = [r.perm_id for r in relations]
        return Permission.objects.filter(id__in=perm_id_list)

    def has_permission(self, perm_name):
        """
        检查该角色是否具有某权限
        @param perm_name: 权限名称
        @return: True or False
        """
        try:
            perm = Permission.get(name=perm_name)
        except Permission.DoseNotExist:
            return False
        else:
            return RolePermissionRelation.objects.filter(role_id=self.id, perm_id=perm.id).exists


class Permission(UdmModel):
    name = models.CharField(max_length=64, unique=True, verbose_name=_("权限名称"))
    url = models.CharField(max_length=64, blank=True, null=True, verbose_name=_("URL地址"))
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=1, verbose_name=_('状态'))
    desc = models.CharField(max_length=256, blank=True, null=True, verbose_name=_("描述"))



class UserRoleRelation(UdmModel):
    user_id = models.PositiveSmallIntegerField()
    role_id = models.PositiveSmallIntegerField()


class RolePermissionRelation(UdmModel):
    role_id = models.PositiveSmallIntegerField()
    perm_id = models.PositiveSmallIntegerField()


class UserPermissionRelation(UdmModel):
    user_id = models.PositiveSmallIntegerField()
    perm_id = models.PositiveSmallIntegerField()
