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
    $('#menu dt a').css('width', '62px');
}

function init_keyboard_shortcuts() {
    $(document).bind('keydown', 'ctrl+s', function() {
        $('.primaryAction').click();
    });
}

function init_code_editor() {
    if ($('#code_editor').html() != "") {
        language = ($('#id_language').val())
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

function init_wysiwyg_editor() {
    new nicEditor({
        iconsPath : '/content/platform/admin/nic_edit/nicEditorIcons.gif',
        buttonList : ['bold','italic','underline','strikeThrough','left','center','right','justify','link','unlink','ol','ul','indent','outdent','subscript','superscript','removeformat','xhtml']
    }).panelInstance('wysiwyg_editor');
}

function init_msg() {
    $('.msg .icon').addClass('delete');
    $('.msg').click(function() {
        $(this).slideUp('fast');
    });
}