document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#Events').style.display='none'
    document.querySelector('#Calendar').style.display='none'
    document.querySelector('#Download').style.display='none'
    document.querySelector('#E').addEventListener('click', ()=>load('#Events'));
    document.querySelector('#C').addEventListener('click', ()=>load('#Calendar'));
    document.querySelector('#D').addEventListener('click', ()=>load('#Download'));
    if(document.querySelector('#alert')!=null)
        alert(document.querySelector('#alert').innerHTML);
});


function load(s) {
    document.querySelector('#Events').style.display='none'
    document.querySelector('#Calendar').style.display='none'
    document.querySelector('#Download').style.display='none'
    document.querySelector(s).style.display='block'
}