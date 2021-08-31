from django.conf.urls import url

from Emp import views
urlpatterns = [
    url('empList/', views.toEmpList, name='empList'),
    url('toEmpListByAjax/', views.toEmpListByAjax, name='toEmpListByAjax'),
]