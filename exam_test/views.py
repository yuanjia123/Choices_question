from django.shortcuts import render
from exam_test import tools
from exam_test.models import Choice
import random
from exam_test.forms import ExcelForm
import os
import time
from django.http import HttpResponse


def index(request):
    # li = tools.data()
    # for i in li:
    #     Choice.objects.create(choice_text=i.get("topic"),a=i.get("a"),b=i.get("b"),c=i.get("c"),d=i.get("d"),answer=i.get("answer"),think=i.get("think"))
    li = Choice.objects.all()[:50]
    return render(request,"index.html",{
        'choices':li
    })



def score(request,random_li,name):
    '''
    把50道题对象传进来 choices
    '''
    ore = 0

    #把传递来的字符串变成列表
    li_2 = []
    for i in random_li.replace("[", "").replace("]", "").replace(" ", "").split(","):
        li_2.append(int(i))
    #print("随机的列表有那些{}, 它的类型{}".format(li_2, type(li_2)))

    #拿到所有的题
    li = list(Choice.objects.all())

    #页面传来的答案
    qian_select_li = []
    for i in range(1, 51):
        d = "d_{}".format(i)
        select = request.POST.get(d)
        qian_select_li.append({i: select})

    #50个题的正确答案
    new_li = []
    for i in li_2:
        new_li.append(li[i-1])
    # print("在提交页面里面、传递过来的随机题目",new_li)

    z = 1
    error_li = []
    success_li = []
    error_question = []
    for j in new_li:
        #答对了
        if qian_select_li[z-1].get(z) == j.answer:
            # print("答对了")
            success_li.append(j)
            ore += 2
        #错误的
        else:
            #把这个错误的答案传递下去
            error_question.append({j.id:qian_select_li[z-1].get(z)})
            #把做错的题传下去
            error_li.append(j)
        z += 1

    print("错误的有：",error_li)
    print("正确的有：",success_li)
    print("打印分数:",ore)
    print("打印错误的题{id:选项}:",error_question)
    return render(request, "score.html", {
        'name':name,
        'score': ore,
        'choice_all_li':new_li,
        'error_li':error_li,
        'success_li':success_li,
        'error_question':error_question,
    })



def question_choice(request,name):

    # 拿到全部的选择题答案
    li = list(Choice.objects.all())

    random_li = []
    for i in range(1,121):
        random_li.append(i)

    # 随机选择50个
    random_li = random.choices(random_li, k=50)

    val_li = []
    for random_choice in random_li:
        val_li.append(li[random_choice-1])

    print("----------------------------------",name,type(name))
    return render(request, "choices_question.html", {
        'choices':val_li,
        'random_li':random_li,
        "name":name
        })


def test(request):
    li = [{1:'A'},{3:"B"},{9:"c"},{10:"D"}]
    return render(request,'test.html',{
        "li":li
    })


def upload(request):
    if request.method == 'POST':
        form = ExcelForm(request.POST,request.FILES)
        #获取文件
        excel_file = request.FILES.get('excel_file')

        #对文件进行重名保存
        file_name = '%d.xlsx' % round(time.time() * 1000)
        #路径
        file_path = os.path.join('excel', file_name)
        print("-----------------------------------",excel_file.name)
        print("-----------------------------------",file_path)

        #如果当前项目下面不存media文件夹、则创建
        if not os.path.exists('media'):
            os.makedirs('media')

        with open(os.path.join(os.getcwd(),'media',excel_file.name),'wb') as fw:
            #如果是小文件 比如图片可以一次上传
            fw.write(excel_file.read())

            #分块读取
            for ck in excel_file.chunks():
                fw.write(ck)

        msg = "文件上传成功"
        return render(request, 'upload.html', {'form': form,'msg':msg})
    else:
        form = ExcelForm()
    return render(request, 'upload.html', {'form': form})
