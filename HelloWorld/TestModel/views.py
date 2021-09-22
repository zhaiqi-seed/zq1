from django.shortcuts import render
from django.contrib import messages
from django.db.models import Count,Max
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

from . import models
from .models import Teacher
from Books import models as bookModels

from Books.models import Book

from Demo.models import DemoList
# Create your views here.
class Leaf:
    id = 0
    pid = 0
    title = ""
    url = ""
    children = []
    spread = ""

    def __init__(self, id, pid, name, url, children):
        self.id = id
        self.pid = pid
        self.title = name
        self.url = url
        self.children = children
        self.spread = 'true'

def dd (list = {}, level = 0, maxlevel = 3, leafTemp = Leaf(0, 0, 'root', '', [])):
    for item in list:
        if level <= maxlevel and  item.level == level and item.pid == leafTemp.id:
            leafT = Leaf(item.id, item.pid, item.name, item.url, [])

            dd(list, level + 1, maxlevel, leafT)

            leafTemp.children.append(leafT)
@csrf_exempt
def getDemoTreeForAjax(request):

    context = {}

    res = DemoList.objects.all()

    res1 = DemoList.objects.aggregate(Max('level'))

    tree2 = Leaf(0, 0, '目录', '', [])

    dd(res, 1, res1['level__max'], tree2)

    str = json.dumps(tree2, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    return JsonResponse(str, safe=False)
#跳转到图书统计页面
def toCountBooks(request):
    context = {}

    leftList = DemoList.objects.all()
    context['demoList'] = leftList

    #目前有多少种书
    res = bookModels.Book.objects.aggregate(c = Count("id"))
    context['bookcount'] = res['c']

    #有多少人看这些书
    res2 = Book.objects.values("teacher__id").distinct().aggregate(c=Count("*"))
    context['peoplecount'] = res2['c']

    #每本书的订阅数
    res3 = Book.objects.values("bookName").annotate(c=Count("teacher__id"))
    context['bookOrderCount'] = res3

    return render(request, 'countbooks.html', context)
#修改师傅的读书信息
@csrf_exempt
def updateBooks(request):

    bookIds = request.POST.getlist('bookIdCheckBox')
    teacherId = request.POST['teacherId']

    teacherbooks = Book.objects.filter(teacher = teacherId)

    for boo in teacherbooks:
        boo.teacher.remove

    newTeacherBooks = Book.objects.filter(id__in = bookIds)

    for bo in newTeacherBooks:
        bo.teacher.add(teacherId)

    print('~~~~~~~~~~~~~~~~~~~~TestModel.views updateBooks teacherId = ' + teacherId)

    messages.add_message(request, messages.SUCCESS, '修改成功')

    context = {}
    context['teacherId'] = teacherId
    personBookList = Book.objects.filter(teacher = teacherId)
    personBookIdList = []
    for book in personBookList:
        personBookIdList.append(book.id)
    context['personBookIdList'] = personBookIdList

    bookList = Book.objects.all()
    context['bookList'] = bookList

    leftList = DemoList.objects.all()
    context['demoList'] = leftList

    return render(request, 'managebooks.html', context)
#跳转到书籍管理
def toManageBooks(request):

    context = {}

    context['teacherId'] = request.POST['pk']
    personBookList = Book.objects.filter(teacher = request.POST['pk'])
    personBookIdList = []
    for book in personBookList:
        personBookIdList.append(book.id)
    context['personBookIdList'] = personBookIdList

    bookList = Book.objects.all()
    context['bookList'] = bookList

    leftList = DemoList.objects.all()
    context['demoList'] = leftList

    return render(request, 'managebooks.html', context)
#通过名称查找教师列表
def getTeacherListByName(request):

    context = {}
    teacherList = models.Teacher.objects.filter(name__contains = (request.POST['name']))
    context['dblist'] = teacherList

    leftList = DemoList.objects.all()
    context['demoList'] = leftList

    return render(request, 'teacherlist.html', context)
#通过名称查找教师列表
@csrf_exempt
def getTeacherListByNameForAjax(request):

    context = {}
    context['code'] = 0

    tealist = models.Teacher.objects.all()

    resultList = []
    for item in tealist:

        res = {}
        res['id'] = item.id
        res['name'] = item.name
        res['age'] = item.age

        resultList.append(res)

    context['data'] = resultList

    return JsonResponse(context, safe=False)
#跳转到修改页面
def toUpdateTeacher(request):

    context = {}

    pk = request.POST['pk']
    teacher = models.Teacher.objects.filter(pk=pk).first()
    context['teacher'] = teacher

    leftList = DemoList.objects.all()
    context['demoList'] = leftList

    return render(request, 'updateteacher.html', context)
#修改师傅信息
@csrf_exempt
def updateTeacher(request):
    pk = request.POST['pk']
    if pk:
        teacher = models.Teacher.objects.filter(pk=pk).first()

        name = request.POST['name']
        age = request.POST['age']
        password = request.POST['password']

        if name:
            teacher.name = name
        if age:
            teacher.age = age
        if password:
            teacher.password = password

        teacher.save()
    print('~~~~~~~~~~~~~~~~~~~~TestModel.views updateTeacher id = ' + pk)

    messages.add_message(request, messages.SUCCESS, '修改成功')
    return searchTeacherList(request)
#修改师傅信息
@csrf_exempt
def updateTeacherByAjax(request):
    pk = request.POST['pk']
    if pk:
        teacher = models.Teacher.objects.filter(pk=pk).first()

        if 'name' in request.POST:

            teacher.name = request.POST['name']

        if 'age' in request.POST:

            teacher.age = request.POST['age']

        if 'password' in request.POST:

            teacher.password = request.POST['password']

        teacher.save()
    print('~~~~~~~~~~~~~~~~~~~~TestModel.views updateTeacherByAjax id = ' + pk)

    context = {}
    context['code'] = 0
    context['message'] = '修改成功'
    return JsonResponse(context, safe=False)
#删除师傅信息
@csrf_exempt
def deleteTeacher(request):
    pk = request.POST['pk']
    teacher = models.Teacher.objects.filter(pk=pk).first()
    teacher.delete()
    print('~~~~~~~~~~~~~~~~~~~~TestModel.views deleteTeacher id = ' + pk)

    messages.add_message(request, messages.SUCCESS, '删除成功')

    return searchTeacherList(request)
#新增师傅信息
@csrf_exempt
def addTeacher(request):

    name = request.POST['name']
    age = request.POST['age']
    password = request.POST['password']
    teacher = models.Teacher(name = name, age = age, password = password)
    teacher.save()
    print('~~~~~~~~~~~~~~~~~~~~TestModel.views addTeacher')

    messages.add_message(request, messages.SUCCESS, '新增成功')

    return searchTeacherList(request)
#查询师傅列表
def searchTeacherList(request):
    rightlist = Teacher.objects.all()

    context = {}
    context['dblist'] = rightlist;

    leftList = DemoList.objects.all()
    context['demoList'] = leftList

    return render(request, 'teacherlist.html', context)
#跳转到新增页面
def toAdd(request):

    context = {}

    leftList = DemoList.objects.all()
    context['demoList'] = leftList

    return render(request, 'addteacher.html', context)

