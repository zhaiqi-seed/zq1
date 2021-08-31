from django.http import HttpResponse
from django.shortcuts import render

from TestModel.models import Test, Teacher

def testdb(request):
    #test1 = Test(id="1",name='runoob')
    #test1.save()
    #return HttpResponse('<p>数据添加成功</p>
    #list =  Test.objects.all()
    list = Teacher.objects.all()
    context = {}
    context['dblist'] = list;
    return render(request, 'db.html', context)