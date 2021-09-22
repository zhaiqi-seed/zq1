function searchFSubmit(){

    document.getElementById("searchF").submit()
}
function toBook(pk) {

    document.getElementById('userId').value = pk

    document.getElementById('bookForm').submit()
}
function updateTeacher(pk) {

    document.getElementById('updateId').value = pk

    document.getElementById('updateForm').submit()
}
function delTeacher(pk) {

    document.getElementById('delId').value = pk

    document.getElementById('delForm').submit()
}

//修改师傅信息的ajax方法
function updateTeacherByAjax(tid, tname) {

    $.ajax({
       url:"/testModel/updateTeacherByAjax/",
       type:"POST",
       //data:{'csrfmiddlewaretoken': csrf_token},
       data:{
           pk : tid,
           name: tname
       },
       success:function(message){

           alert(message.message);
       },         　　　　　　
       error: function (e) {
           console.log("error in teacherlist.js" + e)
       }
    })
}
$(document).ready(function(){

    // 获取到{% csrf_token %}这个模板渲染语法渲染之后的input标签对应的值
    //var csrf_token = $('[name="csrfmiddlewaretoken"]').val();
    /*
    $.ajax({
       url:"/testModel/getTeacherListByNameForAjax/",
       type:"POST",
       //data:{'csrfmiddlewaretoken': csrf_token},
       data:{},
       success:function(message){
           console.log(message.data)
       },         　　　　　　
       error: function () {
           console.log("error in teacherlist.js")
       }
    })

     */
});
