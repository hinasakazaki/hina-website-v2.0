$(document).ready(function() {


    $('.frame1').click(function() {
        /* Actions on thumbnail */
        $('.thumbnail').removeClass('active');
        $(this).addClass('active');
        /* Actions on large image */
        var src = $(this).find('.thumbnail-large').text();
        $('#large-img').find('img').attr('src', src);
    });
    /* Defaults */
    $('.thumbnail:first').addClass('active');
    $('#large-img').find('img').attr('src', 'https://farm8.staticflickr.com/7327/13484724834_12c708d8c5.jpg');



    
});