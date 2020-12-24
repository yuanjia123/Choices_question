from django import forms
from django.forms import widgets
from django.forms import fields

class RegisterForm(forms.Form):
    '''
    账号登录的验证
    '''
    #名称要必须和视图中的名字一样
    name = forms.CharField(label="用户名",required=True,min_length=3)  #required=True必填字段
    email = forms.CharField(label="邮箱",required=True,min_length=3)  #required=True必填字段
    password = forms.CharField(label="密码",required=True,min_length=3)  #required=True必填字段

class LoginForm(forms.Form):
    username = forms.CharField(label="用户名",required=True,min_length=3,)  #required=True必填字段
    username.widget.attrs.update({'class': 'form-control'})

    password = forms.CharField(label="密码",required=True,min_length=3,)  #required=True必填字段
    password.widget.attrs.update({'class': 'form-control'})

class File_Form(forms.Form):
    name = forms.CharField(label="用户名",required=False)
    img = forms.ImageField(label="照片",required=False)  #required=True必填字段


