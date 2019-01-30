/*
********************************************************************************************
Created on : January, 31st, 2018
Developer : Gaurav Bhardwaj
Website: www.ittwist.com
********************************************************************************************
THE BELOW CODE CONTAINS THE CLIENT SIDE CODE OR JAVASCRIPT CODE
FEEL FREE TO USE THE CODE
*/

var modal,span,error;
// This code will trigger the modal of error when the error message will come, otherwise it will be hidden
function onLoadBody () {
    modal = document.getElementById('myModal');
    span = document.getElementsByClassName("close")[0];
    error = document.getElementById('error');
    if (error.value !== "") {
        modal.style.display = "block";
    }
    else {
        modal.style.display = "none";
    }
}
// Code for close button of modal close element
function onClickClose () {
    modal = document.getElementById('myModal');
    modal.style.display = "none";
}