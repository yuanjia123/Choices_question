from django import forms

class LoginForm(forms.Form):
    '''
    账号登录的验证
    '''
    #名称要必须和视图中的名字一样
    username = forms.CharField(label="用户名",required=True,min_length=3)  #required=True必填字段
    password = forms.CharField(label="密码",required=True,min_length=3)  #required=True必填字段

    choices = forms.ChoiceField(choices=((1,"男"),(2,"女")),label="性别")
    time = forms.TimeField()

    url = forms.fields.URLField(label="必须是网址",required=True)
