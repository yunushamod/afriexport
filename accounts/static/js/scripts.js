/*!
* Start Bootstrap - Shop Homepage v5.0.5 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

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