from django import forms
from django.forms import widgets
class ExcelForm(forms.Form):
    '''
    账号登录的验证
    '''
    #名称要必须和视图中的名字一样
    file_name = forms.CharField(label="上传文件名", required=True,min_length=3)  # required 必填字段  required=False 不是必填字段
    file_name.widget.attrs.update({'class': 'form-control', 'id': "exampleInputPassword1",'placeholder':"试题名称"})

    file_excel = forms.FileField(label="上传文件", required=False)  # required 必填字段  required=False 不是必填字段




class AjaxForm(forms.Form):
    username = forms.CharField(
        required=True,
        min_length=3,
        error_messages={
            "min_length":"用户名输入不正确",
        }
    )
    gender = forms.BooleanField(
        widget=widgets.RadioSelect(choices=[(0,"男"),(1,"女"),]),
        required=False
    )