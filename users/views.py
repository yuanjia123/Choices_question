from django.shortcuts import render
from django.views.generic.base import View
from users.forms import LoginForm
from django.http import HttpResponse


# class Login(View):
#     def get(self, request, *args, **kwargs):
#         return render(request,"login.html")

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        msg = "已经完成数据提交"
        if form.is_valid():
            user_name = form.cleaned_data["username"]
            pass_word = form.cleaned_data["password"]
            choices = form.cleaned_data["choices"]
            print("user_name:   ",user_name)
            print("pass_word:   ",pass_word)
            print("choices:   ",choices)



    else:
        form = LoginForm()
        # msg = "初始化表单"

    return render(request,'login.html',{'form':form})


# 表单
def search_form(request):
    return render(request, 'search_form.html')


# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)