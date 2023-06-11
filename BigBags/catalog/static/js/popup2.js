$( document ).ready(function() {
    $('#popup_script').on('click', function(e) {
        console.log(123);
        $('#popup_bg').fadeIn(600);
    });
    $('.close-popup').on('click', function() {
        $('#popup_bg').fadeOut(600);
    });
});