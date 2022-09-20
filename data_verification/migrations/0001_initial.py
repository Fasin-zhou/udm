# Generated by Django 3.2.14 on 2022-08-22 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataBatchDetailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blind_numbering', models.CharField(max_length=50, null=True, verbose_name='病例编盲号')),
                ('detail_number', models.IntegerField(null=True, verbose_name='数量')),
                ('device_brand', models.CharField(max_length=50, null=True, verbose_name='设备品牌')),
                ('device_model', models.CharField(max_length=50, null=True, verbose_name='设备型号')),
                ('age', models.IntegerField(null=True, verbose_name='年龄')),
                ('sex', models.IntegerField(choices=[('0', '女'), ('1', '男')], null=True, verbose_name='性别 0女 1男')),
                ('application_scene', models.CharField(max_length=128, null=True, verbose_name='应用场景')),
                ('cases_level', models.CharField(max_length=128, null=True, verbose_name='病例分级')),
                ('clinic_diagnosis', models.CharField(max_length=500, null=True, verbose_name='临床诊断')),
                ('check_date', models.DateTimeField(null=True, verbose_name='检查时间')),
                ('ultrasonic_report', models.CharField(max_length=500, null=True, verbose_name='超声报告')),
                ('diagnosis_date', models.DateTimeField(null=True, verbose_name='诊断时间')),
                ('pathology_report', models.CharField(max_length=500, null=True, verbose_name='病理报告')),
                ('molding', models.CharField(max_length=128, null=True, verbose_name='亚型')),
                ('remarks', models.CharField(max_length=500, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '批次信息',
                'db_table': 'date_batch_detail',
            },
        ),
        migrations.CreateModel(
            name='DataBatchModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receive_date', models.DateTimeField(null=True, verbose_name='接收日期')),
                ('batch_number', models.CharField(max_length=50, null=True, verbose_name='数据批号')),
                ('source', models.CharField(max_length=50, null=True, verbose_name='数据来源')),
                ('cases_number', models.IntegerField(null=True, verbose_name='病例数量')),
                ('file_number', models.IntegerField(null=True, verbose_name='文件数量')),
                ('data_usage', models.CharField(max_length=500, null=True, verbose_name='数据用途')),
                ('verify_status', models.IntegerField(choices=[('0', ''), ('1', '进行中'), ('2', '待评审'), ('3', '评审不通过'), ('4', '评审通过')], null=True, verbose_name="当前状态(''、进行中、待评审、评审不通过、评审通过)")),
            ],
            options={
                'verbose_name': '数据批次',
                'db_table': 'date_batch',
            },
        ),
        migrations.CreateModel(
            name='DataVerificationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_file_path', models.CharField(max_length=128, null=True, verbose_name='Data_file_path')),
                ('blind_numbering', models.IntegerField(null=True, verbose_name='Bilnd_numbering')),
                ('quantity_check', models.CharField(choices=[('qualify', '合格'), ('unqualify', '不合格')], max_length=16, null=True, verbose_name='Quantity_check')),
                ('form_check', models.CharField(choices=[('qualify', '合格'), ('unqualify', '不合格')], max_length=16, null=True, verbose_name='Form_check')),
                ('format_check', models.CharField(choices=[('qualify', '合格'), ('unqualify', '不合格')], max_length=16, null=True, verbose_name='Format_check')),
                ('resolution_check', models.CharField(choices=[('qualify', '合格'), ('unqualify', '不合格')], max_length=16, null=True, verbose_name='Resolution_check')),
                ('size_check', models.CharField(choices=[('qualify', '合格'), ('unqualify', '不合格')], max_length=16, null=True, verbose_name='Size_check')),
                ('blind_check', models.CharField(choices=[('qualify', '合格'), ('unqualify', '不合格')], max_length=16, null=True, verbose_name='Blind_check')),
                ('case_duplication', models.CharField(choices=[('qualify', '合格'), ('unqualify', '不合格')], max_length=16, null=True, verbose_name='Case_duplication')),
                ('image_duplication', models.CharField(choices=[('qualify', '合格'), ('unqualify', '不合格')], max_length=16, null=True, verbose_name='Image_duplication')),
                ('name_duplication', models.CharField(choices=[('qualify', '合格'), ('unqualify', '不合格')], max_length=16, null=True, verbose_name='Name_duplication')),
            ],
            options={
                'verbose_name': '数据校验',
                'db_table': 'date_verification',
            },
        ),
    ]
