from django import forms

class ExcelForm(forms.Form):
    '''
    账号登录的验证
    '''
    #名称要必须和视图中的名字一样
    excel_file = forms.FileField(label="上传文件",required=False)  #required=True必填字段





