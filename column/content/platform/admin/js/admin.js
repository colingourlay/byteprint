function init_collapsible_menu() {
    $('#menu dd').hide()
    $('#menu dd ul li.current').parent().parent().show()
    $('#menu dt').addClass('closed');
    $('#menu dd ul li.current').parent().parent().prev().removeClass('closed');
    $('#menu dt .toggle').show();
    $('#menu dt .toggle').click(function(){
        if ($(this).parent().hasClass('closed')) {
            $(this).parent().removeClass('closed');
            $(this).parent().next().slideDown('fast');
        } else {
            $(this).parent().next().slideUp('fast', function() {
                $(this).prev().addClass('closed');
            });
        }
    });
}

function init_msg_close_buttons() {
    $('.msg .close').click(function(){
        $(this).parent().slideUp('fast', function() {
            $(this).remove();
        });
    });
}

$(document).ready(function(){
    init_collapsible_menu();
    init_msg_close_buttons();
});