from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from register.models import linedata, softdata
from django.conf import settings
import csv,codecs
from datetime import datetime
# Register your models here.



exportable_fields = ('job_name', 'describe_name', 'operator_name', 'delay_date', 'contract_time', 'cost', 'bandwidth_size', 'supplier_name', 'master_people', 'email_address')
exportable_fields2 = ('job_name', 'delay_date', 'cost', 'master_people')
email_people = {'email_address'}
email_people_soft = {'email_address_soft'}
email_show_list = ('soft_name', 'contract_time_soft', 'delay_date_soft', 'master_people_soft')
def export_model_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response.write(codecs.BOM_UTF8) #解决导出excel中文乱码问题，import csv处增加codecs，再增加本行内容。
    field_list = exportable_fields
    response['Content-Disposition'] = 'attachment; filename=%s-list-%s.csv' % (
        'data',
        datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),
    )

    # 写入表头
    writer = csv.writer(response)
    writer.writerow(
        [queryset.model._meta.get_field(f).verbose_name.title() for f in field_list],
    )

    for obj in queryset:
        ## 单行 的记录（各个字段的值）， 根据字段对象，从当前实例 (obj) 中获取字段值
        csv_line_values = []
        for field in field_list:
            field_object = queryset.model._meta.get_field(field)
            field_value = field_object.value_from_object(obj)
            csv_line_values.append(field_value)
        writer.writerow(csv_line_values)


    return response
def export_model_as_email1(modeladmin, request, queryset):
    field_list1 = email_people
    field_list2 = exportable_fields2
    for obj in queryset:
        ## 单行 的记录（各个字段的值）， 根据字段对象，从当前实例 (obj) 中获取字段值
        email_line_values = []
        for field in field_list2:
            field_object = queryset.model._meta.get_field(field)
            field_value = field_object.value_from_object(obj)
            email_line_values.append(field_value)
    for obj2 in queryset:
        sendemail_line_values = []
        for field2 in field_list1:
            field_object2 = queryset.model._meta.get_field(field2)
            field_value2 = field_object2.value_from_object(obj2)
            sendemail_line_values.append(field_value2)
    send_mail(subject='MST信息登记系统发来的消息',
              message='您好，您负责的专线%s将于一个月后到期，请注意续费或处理！！' % (email_line_values,),
              from_email='ryan.wang@miniso.com',
              recipient_list= sendemail_line_values,
              fail_silently=False)
    return HttpResponse('邮件发送成功')

exportable_fields_soft = ('soft_name', 'contract_time_soft', 'delay_date_soft', 'number_of', 'cost_single', 'cost_soft', 'license_type', 'supplier_name_soft', 'master_people_soft', 'email_address_soft')
def export_model_as_csv_soft(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response.write(codecs.BOM_UTF8) #解决导出excel中文乱码问题，import csv处增加codecs，再增加本行内容。
    field_list_soft = exportable_fields_soft
    response['Content-Disposition'] = 'attachment; filename=%s-list-%s.csv' % (
        'data',
        datetime.now().strftime('%Y-%m-%d-%H-%M-%S'),
    )

    # 写入表头
    writer = csv.writer(response)
    writer.writerow(
        [queryset.model._meta.get_field(f).verbose_name.title() for f in field_list_soft],
    )

    for obj in queryset:
        ## 单行 的记录（各个字段的值）， 根据字段对象，从当前实例 (obj) 中获取字段值
        csv_line_values_soft = []
        for field_soft in field_list_soft:
            field_object = queryset.model._meta.get_field(field_soft)
            field_value = field_object.value_from_object(obj)
            csv_line_values_soft.append(field_value)
        writer.writerow(csv_line_values_soft)


    return response

def export_model_as_email1_soft(modeladmin, request, queryset):
    field_list3 = email_people_soft
    field_list4 = email_show_list
    for obj in queryset:
        ## 单行 的记录（各个字段的值）， 根据字段对象，从当前实例 (obj) 中获取字段值
        email_line_values_soft = []
        for field_soft_email in field_list4:
            field_object = queryset.model._meta.get_field(field_soft_email)
            field_value = field_object.value_from_object(obj)
            email_line_values_soft.append(field_value)
    for obj2 in queryset:
        sendemail_line_values_soft = []
        for field2 in field_list3:
            field_object2 = queryset.model._meta.get_field(field2)
            field_value2 = field_object2.value_from_object(obj2)
            sendemail_line_values_soft.append(field_value2)
    send_mail(subject='MST信息登记系统发来的消息',
              message='您好，您负责的软件%s将于一个月后到期，请注意续费或处理！！' % (email_line_values_soft,),
              from_email='ryan.wang@miniso.com',
              recipient_list= sendemail_line_values_soft,
              fail_silently=False)
    return HttpResponse('邮件发送成功')
    
export_model_as_csv.short_description = u'导出为CSV文件'
export_model_as_csv_soft.short_description = u'导出为CSV文件'
export_model_as_email1.short_description = u'发送邮件通知'
export_model_as_email1_soft.short_description = u'发送邮件通知'
class linedataAdmin(admin.ModelAdmin):
    actions = (export_model_as_csv,export_model_as_email1,)
    list_display = ('job_name', 'describe_name', 'operator_name', 'contract_time', 'delay_date', 'cost', 'bandwidth_size', 'supplier_name', 'master_people', 'email_address')
    search_fields = ('job_name', 'describe_name', 'operator_name', 'contract_time', 'delay_date', 'cost', 'bandwidth_size', 'supplier_name', 'master_people', 'email_address')
class softdataAdmin(admin.ModelAdmin):
    actions = (export_model_as_csv_soft, export_model_as_email1_soft,)
    list_display = ('soft_name', 'contract_time_soft', 'delay_date_soft', 'number_of', 'cost_single', 'cost_soft', 'license_type', 'supplier_name_soft', 'master_people_soft', 'email_address_soft')
    search_fields = ('soft_name', 'contract_time_soft', 'delay_date_soft', 'number_of', 'cost_single', 'cost_soft', 'license_type', 'supplier_name_soft', 'master_people_soft', 'email_address_soft')
admin.site.register(linedata, linedataAdmin)
admin.site.register(softdata, softdataAdmin)