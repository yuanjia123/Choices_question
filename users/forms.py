from django import forms

class RegisterForm(forms.Form):
    '''
    账号登录的验证
    '''
    #名称要必须和视图中的名字一样
    name = forms.CharField(label="用户名",required=True,min_length=3)  #required=True必填字段
    email = forms.CharField(label="邮箱",required=True,min_length=3)  #required=True必填字段
    password = forms.CharField(label="密码",required=True,min_length=3)  #required=True必填字段

class LoginForm(forms.Form):
    name = forms.CharField(label="用户名",required=True,min_length=3)  #required=True必填字段
    password = forms.CharField(label="密码",required=True,min_length=3)  #required=True必填字段


class File_Form(forms.Form):
    name = forms.CharField(label="用户名",required=False)
    img = forms.ImageField(label="照片",required=False)  #required=True必填字段


