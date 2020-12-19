from django.db import models

# Create your models here.
class userinfo(models.Model):
    uid = models.CharField(max_length=10,verbose_name="用户名",help_text='用户名由英文字母、下划线数字组成')
    password = models.CharField(max_length=6,verbose_name="密码",help_text='登录密码由6-8位字符组成')
    email = models.CharField(max_length=30,verbose_name="Email",help_text='有效电子邮箱地址')