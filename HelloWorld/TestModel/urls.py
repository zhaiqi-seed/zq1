from django.conf.urls import url

from TestModel import views
urlpatterns = [
    url('getDemoTreeForAjax/', views.getDemoTreeForAjax, name="getDemoTreeForAjax"),
    url('updateTeacherByAjax/', views.updateTeacherByAjax, name="updateTeacherByAjax"),
    url('toCountBooks/', views.toCountBooks, name="toCountBooks"),
    url('updateBooks/', views.updateBooks, name="updateBooks"),
    url('toManageBooks/', views.toManageBooks, name="toManageBooks"),
    url('getTeacherListByName/', views.getTeacherListByName, name="getTeacherListByName"),
    url('toUpdateTeacher/', views.toUpdateTeacher, name="toUpdateTeacher"),
    url('updateTeacher/', views.updateTeacher, name="updateTeacher"),
    url('delTeacher/', views.deleteTeacher, name="deleteTeacher"),
    url('addTeacher/', views.addTeacher, name='addTeacher'),
    url('toAddTeacher/', views.toAdd, name="toAddTeacher"),
    url('teacherList/', views.searchTeacherList, name="teacherList"),
    url('getTeacherListByNameForAjax/', views.getTeacherListByNameForAjax, name="getTeacherListByNameForAjax"),
]