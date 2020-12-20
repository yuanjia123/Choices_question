from django.shortcuts import render,redirect
from django.views.generic.base import View
from users.forms import LoginForm,RegisterForm,File_Form
from django.http import HttpResponse
from users.models import Grade,User,Student

# class Login(View):
#     def get(self, request, *args, **kwargs):
#         return render(request,"register.html")

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        msg = "已经完成数据提交"
        if form.is_valid():
            grade = form.cleaned_data["grade"]

            name = form.cleaned_data["name"]
            age = form.cleaned_data["age"]
            gender = form.cleaned_data["gender"]
            password = form.cleaned_data["password"]
            print("grade:   ",grade)
            print("name:   ",name)
            print("age:   ",age)
            print("gender:   ",gender)
            print("password:   ",password)

            g1 = User.objects.filter(name=name).first()
            if g1:
                msg = "您所输入姓名:{} 已经存在".format(name)
                return render(request, 'register.html', {'form': form, 'msg':msg})
            else:
                msg = "注册成功"
                g1 = Grade(g_name = grade)
                g1.save()
                User.objects.create(name=name,age=age,password=password,g=g1)
                return render(request, 'register.html', {'form': form, 'msg': msg})

    else:
        form = RegisterForm()
        # msg = "初始化表单"

    return render(request, 'register.html', {'form':form})



def login(request):
    if request.method == 'POST':

        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            password = form.cleaned_data["password"]

            g1 = User.objects.filter(name=name,password=password).first()
            if g1:
                msg = "登录成功"
                return redirect("question",name)
            else:
                msg = "账号密码输入错误、请您重新登录"
                return render(request, 'login.html', {'form': form, 'msg': msg})

    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


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

def upload_img(request):
    if request.method == "POST":
        form = File_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            img = request.FILES.get('img')
            Student.objects.create(sname=name,photo=img)
            msg = "上传成功"
        return render(request, 'upload_img.html', {'form':form,'msg':msg })
    else:
        form = File_Form()
        return render(request, 'upload_img.html', {'form': form})

def showall_img(request):
    s_all = Student.objects.all()
    return render(request, 'showall_img.html', {'s_all': s_all})
