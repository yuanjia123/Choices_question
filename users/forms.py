from django import forms
from django.forms import widgets
from django.forms import fields

class RegisterForm(forms.Form):
    '''
    账号登录的验证
    '''
    username = forms.CharField(label="用户名", required=True, min_length=3, )  # required=True必填字段
    #声明username的输入框class=form-control
    username.widget.attrs.update({'class': 'form-control','placeholder':'用户名'})

    #widget=forms.PasswordInput()  申明他是一个type='password'类型
    password = forms.CharField(label="密码", required=True, min_length=3,
                               widget=forms.PasswordInput())  # required=True必填字段
    password.widget.attrs.update({'class': 'form-control','placeholder':'密码'})

    email = forms.CharField(label="邮箱", required=True, min_length=3)
    email.widget.attrs.update({'class': 'form-control','placeholder':'邮箱'})

class LoginForm(forms.Form):
    username = forms.CharField(label="用户名",required=True,min_length=3)  #required=True必填字段
    username.widget.attrs.update({'class': 'form-control','placeholder':'用户名'})

    password = forms.CharField(label="密码",required=True,min_length=3,widget=forms.PasswordInput())  #required=True必填字段
    password.widget.attrs.update({'class': 'form-control','placeholder':'密码'})

class File_Form(forms.Form):
    name = forms.CharField(label="用户名",required=False)
    img = forms.ImageField(label="照片",required=False)  #required=True必填字段


