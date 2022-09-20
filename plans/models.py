from django.db import models
from db_manage.models import DBmanageModel
from django.db.models import DEFERRED
from django.utils.translation import ugettext_lazy as _
from django.db.models.fields import Field

# Create your models here.
class PlansModel(models.Model):
    CURRENTSTATE_CHOICE = [
        ('0','未开始'),
        ('1','进行中'),
        ('2','暂停'),
        ('3','挂起'),
        ('4','完成')
    ]
    plans_code = models.CharField(max_length=50, null=True, verbose_name=_("计划代码/编号（编码规则迎合质控要求）"))
    plans_name = models.CharField(max_length=255, null=True, verbose_name=_("计划名称"))
    plans_begindate = models.DateTimeField(null=True, verbose_name=_("计划开始时间"))
    plans_enddate = models.DateTimeField(null=True, verbose_name=_("计划结束时间（预设）"))
    complete_date = models.DateTimeField(null=True, verbose_name=_("实际完工时间"))
    target_datanumber = models.CharField(max_length=50, null=True, verbose_name=_("目标数据量（可能是例，可能是张）"))
    target_accuracy = models.CharField(max_length=50, null=True, verbose_name=_("目标准确率"))
    plan_usernumber = models.CharField(max_length=50, null=True, verbose_name=_("计划参与人数"))
    algorithm_code = models.CharField(max_length=50, null=True, verbose_name=_("对应算法版本编号"))
    algorithm_accuracy = models.CharField(max_length=50, null=True, verbose_name=_("算法准确率"))
    current_state = models.IntegerField(choices=CURRENTSTATE_CHOICE, null=True, verbose_name=_("当前状态(未开始、进行中、暂停、挂起、完成)"))
    remarks = models.CharField(max_length=500, null=True, verbose_name=_("备注、描述"))
    createuserid = models.IntegerField(null=True, verbose_name=_("创建人ID"))
    modifyuserid = models.IntegerField(null=True, verbose_name=_("修改人ID"))
    freezeuserid = models.IntegerField(null=True, verbose_name=_("冻结计划的用户id"))
    freezeflag = models.IntegerField(null=True, verbose_name=_("冻结标记 0 未冻结 1 冻结"))
    freezedate = models.CharField(max_length=50, null=True, verbose_name=_("冻结时间"))
    freezesavepath = models.CharField(max_length=255, null=True, verbose_name=_("冻结数据保存路径"))
    class Meta:
        db_table = 'plans'
        verbose_name = "计划表"

    def set_db_table(self):
        """
        新项目的实现是直接通过此函数关联到新表
        """
        from django.db.models.expressions import Col
        self._meta.db_table = DBmanageModel.objects.values('plans_tablename')[0]["plans_tablename"]
        for field in self._meta.fields:
            field.cached_col = Col(self._meta.db_table, field)
        