$(document).ready(function() {
    $(window).scroll(function() {
        if($(document).scrollTop() > 107) {
            $('#header').slideUp();
            $('#header2').show();

        }
        else {
            $('#header').show();
            $('#header2').hide();
        }
    });
        
});