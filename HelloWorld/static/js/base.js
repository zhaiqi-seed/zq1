layui.use('tree', function(){

    $.ajax({
       url:"/testModel/getDemoTreeForAjax/",
       type:"POST",
       async:false,
        dataType:"json",
       //data:{'csrfmiddlewaretoken': csrf_token},
       data:{},
       success:function(resi){

            var tree = layui.tree;

            var inst1 = tree.render({
                elem: '#test1',  //绑定元素
                data: eval("[" + resi + "]"),
                //accordion: true,
                //onlyIconControl:true,
                click:function(obj) {
                    url = obj.data.url;

                    console.info(url);

                    if (url != ""){

                        $("#urlForm").attr("action", url);
                        $("#urlForm").submit();
                    }
                }
            });
       },         　　　　　　
       error: function () {
           console.log("error in teacherlist.js")
       }
    })


});

$(document).ready(function(){

    // 获取到{% csrf_token %}这个模板渲染语法渲染之后的input标签对应的值
    //var csrf_token = $('[name="csrfmiddlewaretoken"]').val();
    /*


     */
});