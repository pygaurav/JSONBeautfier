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
        document.getElementsByClassName("top-marg")[0].style.display = "none";
        document.getElementsByClassName("copybutton")[0].style.display = "none";
        document.getElementsByClassName("back")[0].style.display = "none";
        modal.style.display = "block";
    }
    else {
        modal.style.display = "none";
    }
}
// Code for close button of modal close element
function onClickClose () {
    location.href="/";
}
function copyFunc() {
  /* Get the text field */
  var copyText = document.getElementsByTagName("pre")[0].innerHTML;

  /* Select the text field */
  var textArea = document.createElement("textarea");
    textArea.value = copyText;
    document.body.appendChild(textArea);
    textArea.select();
      document.execCommand("copy");
    textArea.remove();

  /* Copy the text inside the text field */


  /* Alert the copied text */
 document.getElementById("copy").innerHTML = "Copied";
 document.getElementById("copy").style ="color:green"
}
