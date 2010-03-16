function init_collapsible_menu() {
    $('#menu dd').hide();
    $('#menu dd ul li.current').parent().parent().show();
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
    $('#menu dt a').css('width', '62px');
}

function init_keyboard_shortcuts() {
    $(document).bind('keydown', 'ctrl+s', function() {
        $('.primaryAction').click();
    });
}

function init_code_editor() {
    if ($('#code_editor').length != 0) {
        language = $('#id_language').val();
        editAreaLoader.init({
            id: "code_editor",
            start_highlight: true,
            min_height: 300,
            allow_resize: "no",
            allow_toggle: false,
            replace_tab_by_spaces: 4,
            word_wrap: true,
            language: "en",
            syntax: language,
            toolbar: "select_font, word_wrap, fullscreen"
        });
        $('#id_language').change(function () {
           editAreaLoader.execCommand(
               'code_editor',
               'change_syntax',
               $('#id_language').val()
           );
        });
    }
}

function init_tinymce() {
    if ($('#id_content').length != 0) {
        $('#id_content').tinymce({
            script_url : '/content/platform/admin/tiny_mce/tiny_mce.js',
            theme : "advanced",
            skin : "o2k7",
            plugins : "style,advimage,inlinepopups,media,pdw,contextmenu,visualchars,xhtmlxtras",
            theme_advanced_buttons1 : "bold,italic,strikethrough,|,justifyleft,justifycenter,justifyright,|,bullist,numlist,|,link,unlink,|,image,|,code,|,pdw_toggle",
            theme_advanced_buttons2 : "underline,|,justifyfull,formatselect,forecolor,|,outdent,indent,|,media,charmap",
            theme_advanced_buttons3 : "",
            theme_advanced_buttons4 : "",
            theme_advanced_toolbar_location : "top",
            theme_advanced_toolbar_align : "left",
            theme_advanced_statusbar_location : "bottom",
            theme_advanced_resizing : true,
            pdw_toggle_on : 1,
            pdw_toggle_toolbars : "2,3,4",
            height : '300',
            width : '600',
        });
    }
}

function init_msg() {
    $('.msg .icon').addClass('delete');
    $('.msg').live('click', function() {
        $(this).slideUp('fast');
    });
}