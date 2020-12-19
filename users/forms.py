from django import forms

class RegisterForm(forms.Form):
    '''
    账号登录的验证
    '''
    #名称要必须和视图中的名字一样
    grade = forms.CharField(label="班级",required=True,min_length=3)  #required=True必填字段
    name = forms.CharField(label="用户名",required=True,min_length=3)  #required=True必填字段
    age = forms.CharField(label="年龄",required=True)  #required=True必填字段
    gender = forms.ChoiceField(choices=((1, "男"), (2, "女")), label="性别")
    password = forms.CharField(label="密码",required=True,min_length=3)  #required=True必填字段

class LoginForm(forms.Form):
    name = forms.CharField(label="用户名",required=True,min_length=3)  #required=True必填字段
    password = forms.CharField(label="密码",required=True,min_length=3)  #required=True必填字段


