from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
# Create your models here.
class DBmanageModel(models.Model):
    plans_tablename = models.CharField(max_length=50, verbose_name=_("当前使用数据表名"))

    class Meta:
        db_table = "db_manage"
        verbose_name = "数据路由表"
