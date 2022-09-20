from django.db import models
from django.utils.translation import ugettext_lazy as _
from common.mixins.models import UdmBaseModel

__all__ = ["DataBatch", "DataDetail"]


class DataBatch(UdmBaseModel):
    """
    数据批次
    """
    STATUS_CHOICES = (
        ('waiting', '待评审'),
        ('running', '评审中'),
        ('passed', '评审通过'),
        ('fail', '评审不通过'),
    )
    received_time = models.DateTimeField(verbose_name=_('Received time'))
    data_batch_number = models.CharField(max_length=128, unique=True, verbose_name=_('Data batch number'))
    data_resource = models.CharField(max_length=64, verbose_name=_('Data resource'))
    case_number = models.PositiveIntegerField(blank=True, null=True, verbose_name=_('Number of cases'))
    image_number = models.PositiveIntegerField(verbose_name=_('Number of images'))
    verify_status = models.CharField(
        max_length=64, choices=STATUS_CHOICES, db_index=True, verbose_name=_('Verify status')
    )
    pretreatment_status = models.CharField(
        max_length=64, choices=STATUS_CHOICES, db_index=True, verbose_name=_('pretreatment status')
    )

    def __str__(self):
        return str(self.data_batch_number)


class DataDetail(UdmBaseModel):
    """
    数据明细
    """
    batch = models.ForeignKey(
        'image_annotation.DataBatch', to_field='data_batch_number', on_delete=models.SET_NULL, null=True, db_constraint=False
    )
    # TODO:是否唯一待定
    blind_number = models.CharField(max_length=128, unique=True, verbose_name=_('Blind number'))
    image_name = models.CharField(max_length=128, verbose_name=_('Image name'))
    original_case_number = models.CharField(max_length=128, unique=True, verbose_name=_('original case number'))