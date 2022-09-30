let formTags = document.querySelectorAll('input');
formTags.forEach((form) => {
    if(form.type == 'checkbox'){
        form.classList.add('form-check-input');
    }else{
        form.classList.add('form-control');
    }
});
let selectLists = document.querySelectorAll('select');
selectLists.forEach((selectList) => selectList.classList.add('form-select'))
let textareas = document.querySelectorAll('textarea');
textareas.forEach((textarea) => textarea.classList.add('form-control'));