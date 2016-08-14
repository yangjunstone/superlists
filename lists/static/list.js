jQuery(document).ready(function($) {
    console.log("register keypress event call-back");
    $('input').keypress(function(event){
        console.log("received keypress event");
        $('.has-error').hide();
    });
});