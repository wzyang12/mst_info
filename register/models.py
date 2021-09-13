from django.db import models
from datetime import  datetime
import django.utils.timezone as timezone


class linedata(models.Model):
     job_name = models.CharField(max_length=200, blank=False, verbose_name="专线名称")
     describe_name = models.CharField(max_length=200, blank=False, verbose_name="描述")
     operator_name = models.CharField(max_length=200, blank=False, verbose_name="运营商")
     contract_time = models.DateField(verbose_name="合同签订时间", default=datetime.now)
     delay_date = models.DateField(verbose_name="到期时间", default=datetime.now)
     cost = models.CharField(max_length=200, blank=False, verbose_name="价格")
     bandwidth_size = models.CharField(max_length=200, blank=False, verbose_name="带宽大小(M)")
     supplier_name = models.CharField(max_length=200, blank=False, verbose_name="供应商名称")
     master_people =  models.CharField(max_length=200, blank=False, verbose_name="负责人")
     email_address =  models.CharField(max_length=200, blank=False, verbose_name="邮箱地址")
     class Meta:
          verbose_name = '网络专线记录'
          verbose_name_plural = '网络专线记录'

class softdata(models.Model):
     soft_name = models.CharField(max_length=200, blank=False, verbose_name="软件名称")
     contract_time_soft = models.DateField(verbose_name="合同签订时间", default=datetime.now)
     delay_date_soft = models.DateField(verbose_name="到期时间", default=datetime.now)
     number_of = models.CharField(max_length=200, blank=False, verbose_name="数量(套)")
     cost_single = models.CharField(max_length=200, blank=False, verbose_name="单价")
     cost_soft = models.CharField(max_length=200, blank=False, verbose_name="总价格")
     license_type = models.CharField(max_length=200, blank=False, verbose_name="许可类型")
     supplier_name_soft = models.CharField(max_length=200, blank=False, verbose_name="供应商名称")
     master_people_soft =  models.CharField(max_length=200, blank=False, verbose_name="负责人")
     email_address_soft =  models.CharField(max_length=200, blank=False, verbose_name="邮箱地址")
     class Meta:
          verbose_name = '软件记录'
          verbose_name_plural = '软件记录'