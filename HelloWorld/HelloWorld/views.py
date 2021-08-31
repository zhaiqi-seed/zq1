from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
import datetime

from TestModel.models import Teacher
from Demo.models import DemoList
import sys

import tkinter.messagebox

def toDateBaseTime(request):
    return render(request, 'dateBaseTime.html')
def checkUser(request):

    context = {}
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        try:
            teac = Teacher.objects.get(name=username, password=password)

            if teac:
                rightlist = Teacher.objects.all()
                context['dblist'] = rightlist;

                leftList = DemoList.objects.all()
                context['demoList'] = leftList

                return render(request, 'teacherlist.html', context)
            else:

                messages.add_message(request, messages.ERROR, '用户名或密码不存在')
                return render(request, 'login.html', context)
        except Exception:

            print("~~~~~~~~~~~~~~~~~~~~~~~~~~HelloWorld.views.py checkUser Exception: ",)
            print(sys.exc_info())

            messages.add_message(request, messages.ERROR, '用户名或密码不存在')

            return render(request, 'login.html', context)
    return render(request, 'login.html', context)
def login(request):
    return render(request, 'login.html')
def hello(request):
    return HttpResponse("Hello world ! ")
def runoob(request):
    context = {}
    context['hello'] = 'Hello zq!'
    context['team'] = {'a' : 3, 'b' : 4, 'c' : 5}
    now = datetime.datetime.now()
    context['date'] = now
    context['num'] = 42
    context['numlist'] = (1, 2, 3, 4, 5, 6)
    context['numberD'] = {'1': 11, '2' : 22, "3" : 33}
    context['emptylist'] = ()
    return render(request, 'runoob.html', context)
