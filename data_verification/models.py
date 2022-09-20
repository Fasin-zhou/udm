from email.mime import application
from tabnanny import verbose
from unittest import case
from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class DataVerificationModel(models.Model):
    CHECK_CHOICE = [
        ('qualify','合格'),
        ('unqualify','不合格'),
    ]
    data_file_path = models.CharField(max_length=128, null=True, verbose_name=_("Data_file_path"))
    blind_numbering = models.IntegerField(null=True, verbose_name=_("Bilnd_numbering"))
    quantity_check = models.CharField(max_length=16, null=True, choices=CHECK_CHOICE, verbose_name=_("Quantity_check"))
    form_check = models.CharField(max_length=16, null=True, choices=CHECK_CHOICE, verbose_name=_("Form_check"))
    format_check = models.CharField(max_length=16, null=True, choices=CHECK_CHOICE, verbose_name=_("Format_check"))
    resolution_check = models.CharField(max_length=16, null=True, choices=CHECK_CHOICE, verbose_name=_("Resolution_check"))
    size_check = models.CharField(max_length=16, null=True, choices=CHECK_CHOICE, verbose_name=_("Size_check"))
    blind_check = models.CharField(max_length=16, null=True, choices=CHECK_CHOICE, verbose_name=_("Blind_check"))
    case_duplication = models.CharField(max_length=16, null=True, choices=CHECK_CHOICE, verbose_name=_("Case_duplication"))
    image_duplication = models.CharField(max_length=16, null=True, choices=CHECK_CHOICE, verbose_name=_("Image_duplication"))
    name_duplication = models.CharField(max_length=16, null=True, choices=CHECK_CHOICE, verbose_name=_("Name_duplication"))

    class Meta:
        db_table = "date_verification"
        verbose_name = "数据校验"
    
class DataBatchModel(models.Model):
    VERIFY_STATUS_CHOICE = [
        ('0',''),
        ('1','进行中'),
        ('2','待评审'),
        ('3','评审不通过'),
        ('4','评审通过')
    ]
    receive_date = models.DateTimeField(null=True, verbose_name=_("接收日期"))
    batch_number = models.CharField(max_length=50, null=True, verbose_name=_("数据批号"))
    source = models.CharField(max_length=50, null=True, verbose_name=_("数据来源"))
    cases_number = models.IntegerField(null=True, verbose_name=_("病例数量"))
    file_number = models.IntegerField(null=True, verbose_name=_("文件数量"))
    data_usage = models.CharField(max_length=500, null=True, verbose_name=_("数据用途"))
    verify_status = models.IntegerField(choices=VERIFY_STATUS_CHOICE, null=True, verbose_name=_("当前状态(''、进行中、待评审、评审不通过、评审通过)"))

    class Meta:
        db_table = "date_batch"
        verbose_name = "数据批次"


class DataBatchDetailModel(models.Model):
    SEX_NUM = [
        ('0','女'),
        ('1','男'),
    ]
    blind_numbering = models.CharField(max_length=50, null=True, verbose_name=_("病例编盲号"))
    detail_number = models.IntegerField(null=True, verbose_name=_("数量"))
    device_brand = models.CharField(max_length=50, null=True, verbose_name=_("设备品牌"))
    device_model = models.CharField(max_length=50, null=True, verbose_name=_("设备型号"))
    age = models.IntegerField(null=True, verbose_name=_("年龄"))
    sex = models.IntegerField(choices=SEX_NUM, null=True, verbose_name=_("性别 0女 1男"))
    application_scene = models.CharField(max_length=128, null=True, verbose_name=_("应用场景"))
    cases_level = models.CharField(max_length=128, null=True, verbose_name=_("病例分级"))
    clinic_diagnosis = models.CharField(max_length=500, null=True, verbose_name=_("临床诊断"))
    check_date = models.DateTimeField(null=True, verbose_name=_("检查时间"))
    ultrasonic_report = models.CharField(max_length=500, null=True, verbose_name=_("超声报告"))
    diagnosis_date = models.DateTimeField(null=True, verbose_name=_("诊断时间"))
    pathology_report = models.CharField(max_length=500, null=True, verbose_name=_("病理报告"))
    molding = models.CharField(max_length=128, null=True, verbose_name=_("亚型"))
    remarks = models.CharField(max_length=500, null=True, verbose_name=_("备注"))

    class Meta:
        db_table = "date_batch_detail"
        verbose_name = "批次信息"

