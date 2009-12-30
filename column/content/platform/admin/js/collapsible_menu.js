$(document).ready(function(){
    $('dd').hide()
    $('dd ul li.current').parent().parent().show()
    $('dt').addClass('closed');
    $('dd ul li.current').parent().parent().prev().removeClass('closed');
    $('dt .toggle').show();
    $('dt .toggle').click(function(){
        if ($(this).parent().hasClass('closed')) {
            $(this).parent().removeClass('closed');
            $(this).parent().next().slideDown('fast');
        } else {
            $(this).parent().next().slideUp('fast', function() {
                $(this).prev().addClass('closed');
            });
        }
    });
});