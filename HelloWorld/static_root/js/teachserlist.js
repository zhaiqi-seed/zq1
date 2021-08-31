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

    $("#delId").val(pk)
    document.getElementById('delForm').submit()
}