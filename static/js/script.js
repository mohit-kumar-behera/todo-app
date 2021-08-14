
$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip({delay:{show:400,hide:100}});
});

window.onload = function(){
    path = location.pathname;
    path = path.replace(/\//g,'')
    nav_link_active = document.getElementsByClassName('nav-link active');
    nav_link = document.getElementsByClassName('nav-link');
    if(nav_link_active.length == 1){  //This length should always be one because there can be only one active link
    nav_link_active[0].classList.remove('active');
    }

    if(path == ''){
    nav_link[0].classList.add('active');
    }
    else {
    nav_link[1].classList.add('active');
    } 
}