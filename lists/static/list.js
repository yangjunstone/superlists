jQuery(document).ready(function($) {
    $('input').keypress(function(event){
        console.log("received keypress event");
        $('.has-error').hide();
    });
});