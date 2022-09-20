from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class CasesModel(models.Model):
    SEX_NUM = [
        ('0','女'),
        ('1','男'),
    ]
    CANCELFLAG_CHOICE = [
        ('0','作废'),
        ('1','正常'),
    ]
    DIFFICULTY_CHOICE = [
        ('0','未分类'),
        ('1','容易'),
        ('2','相对容易'),
        ('3','普通'),
        ('4','困难'),
        ('5','特别困难'),
    ]
    inner_code = models.CharField(max_length=50, null=True, verbose_name=_("内部代码，质量体系规则"))
    patient_id = models.CharField(max_length=255, null=True, verbose_name=_("患者编号(ID)"))
    patient_name = models.CharField(max_length=255, null=True, verbose_name=_("患者姓名"))
    exam_hospital = models.CharField(max_length=500, null=True, verbose_name=_("检查医院"))
    hospital_code = models.CharField(max_length=50, null=True, verbose_name=_("医院代码，可关联Hospital表"))
    exam_datetime = models.DateTimeField(null=True, verbose_name=_("检查时间"))
    sex = models.IntegerField(choices=SEX_NUM, null=True, verbose_name=_("性别 0女 1男"))
    age = models.IntegerField(null=True, verbose_name=_("年龄"))
    tel = models.CharField(max_length=50, null=True, verbose_name=_("联系方式"))
    sib_name = models.CharField(max_length=50, null=True, verbose_name=_("家属/联系人姓名"))
    sib_tel = models.CharField(max_length=50, null=True, verbose_name=_("家属联系方式"))
    address = models.CharField(max_length=500, null=True, verbose_name=_("家庭住址"))
    street_address = models.CharField(max_length=500, null=True, verbose_name=_("街道(乡/镇)"))
    village = models.CharField(max_length=500, null=True, verbose_name=_("社区(村)"))
    hepatitis_b_history = models.IntegerField(null=True, verbose_name=_("乙型肝炎病史"))
    hepatitis_c_history = models.IntegerField(null=True, verbose_name=_("丙型肝炎病史"))
    alcoholism_history = models.IntegerField(null=True, verbose_name=_("酗酒病史"))
    hypertension_history = models.IntegerField(null=True, verbose_name=_("高血压病史"))
    diabetes_history = models.IntegerField(null=True, verbose_name=_("糖尿病病史"))
    yqys_history = models.IntegerField(null=True, verbose_name=_("疫区疫水接触史（畜牧区等）"))
    hormone_history = models.IntegerField(null=True, verbose_name=_("激素治疗史"))
    jszlyw_name = models.CharField(max_length=500, null=True, verbose_name=_("激素治疗药物名称"))
    primarytumors_history = models.IntegerField(null=True, verbose_name=_("原发肿瘤病史"))
    primarytumors_name = models.CharField(max_length=255, null=True, verbose_name=_("原发肿瘤病名称"))
    familytumors_history = models.IntegerField(null=True, verbose_name=_("家族恶性肿瘤病史"))
    familytumors_name = models.CharField(max_length=255, null=True, verbose_name=_("家族恶性肿瘤病名称"))
    otherimaging = models.CharField(max_length=500, null=True, verbose_name=_("其他影像学表现"))
    otherimaging_result = models.CharField(max_length=255, null=True, verbose_name=_("其他影像学结果"))
    other_result = models.CharField(max_length=255, null=True, verbose_name=_("其他结果"))
    jaundice = models.IntegerField(null=True, verbose_name=_("有无黄疸"))
    recentfever = models.IntegerField(null=True, verbose_name=_("近期有无发热"))
    recent_abdominalpain = models.IntegerField(null=True, verbose_name=_("近期有无腹痛"))
    weightlessfive_threemonths = models.IntegerField(null=True, verbose_name=_("体重3个月内减轻>5kg"))
    othersy_mptoms = models.IntegerField(null=True, verbose_name=_("其他症状"))
    biopsy = models.IntegerField(null=True, verbose_name=_("有无活检"))
    diagnostic_method = models.CharField(max_length=50, null=True, verbose_name=_("诊断方法"))
    diagnostic_result = models.CharField(max_length=50, null=True, verbose_name=_("诊断结果"))
    otherdiagnostic_result = models.CharField(max_length=50, null=True, verbose_name=_("其他诊断结果"))
    operator_number = models.CharField(max_length=50, null=True, verbose_name=_("操作者编号"))
    file_path = models.CharField(max_length=500, null=True, verbose_name=_("文件路径"))
    cancel_flag = models.IntegerField(choices=CANCELFLAG_CHOICE, null=True, verbose_name=_("作废标识 1：正常 0：作废"))
    batch_number = models.CharField(max_length=50, null=True, verbose_name=_("导入时产生的当前批次号码"))
    videos_number = models.IntegerField(null=True, verbose_name=_("视频数量"))
    tumourfile_number = models.IntegerField(null=True, verbose_name=_("病灶文件数量"))
    tumourmask_number = models.IntegerField(null=True, verbose_name=_("实际病灶数量（注：多发病灶在一个tumourFIle文件中）"))
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICE, null=True, verbose_name=_("图像勾画难易度 0、未分类 1、容易 2、相对容易 3、普通 4、困难 5、特别困难"))
    batchnumber_order = models.IntegerField(null=True, verbose_name=_("批次排序号，排序用"))
    study_code = models.CharField(max_length=50, null=True, verbose_name=_("检查号"))
    device_number = models.CharField(max_length=50, null=True, verbose_name=_("仪器型号"))

    class Meta:
        db_table = "cases"
        verbose_name = "病例表"
    