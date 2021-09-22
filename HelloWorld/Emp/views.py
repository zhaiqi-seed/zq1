from django.shortcuts import render
from django.http import JsonResponse

from Emp.models import Emp
from Demo.models import DemoList
# Create your views here.
def toEmpList(request):

    dict = {}

    leftList = DemoList.objects.all()
    dict['demoList'] = leftList

    return render(request, 'emplist.html', dict)
def toEmpListByAjax(request):

    context = {}
    context['code'] = 0

    emplist = Emp.objects.all()

    resultList = []
    for item in emplist:
        res = {}
        res['id'] = item.id
        res['empName'] = item.empName
        res['teacherName'] = item.teacherid.name

        resultList.append(res)

    context['data'] = resultList

    return JsonResponse(context, safe=False)
