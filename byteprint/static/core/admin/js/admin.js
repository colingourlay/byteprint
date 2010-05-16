function init_collapsible_menu() {
    var menu = {
        "content": $.jStorage.get("byteprint_menu_content", "closed"),
        "design": $.jStorage.get("byteprint_menu_design", "closed"),
        "settings": $.jStorage.get("byteprint_menu_settings", "closed")
    };
    $('#menu dd').hide();
    $('#menu dt').addClass('closed');
    if(menu.content == "open") {
        $('#menu_content').parent().removeClass('closed');
        $('#menu_content').parent().next().show();
    }
    if(menu.design == "open") {
        $('#menu_design').parent().removeClass('closed');
        $('#menu_design').parent().next().show();
    } 
    if(menu.settings == "open") {
        $('#menu_settings').parent().removeClass('closed');
        $('#menu_settings').parent().next().show();
    }
    $.jStorage.set("byteprint_" + $('#menu dd ul li.current').parent().parent().prev().find('a').attr('id'), "open");
    $('#menu dd ul li.current').parent().parent().show();
    $('#menu dd ul li.current').parent().parent().prev().removeClass('closed');
    $('#menu dt .toggle').show();
    $('#menu dt a').css('width', '62px');
    $('#menu dt .toggle').click(function(){
        console.log($(this).prev().attr('id'));
        if ($(this).parent().hasClass('closed')) {
            $.jStorage.set("byteprint_" + $(this).prev().attr('id'), "open");
            $(this).parent().removeClass('closed');
            $(this).parent().next().slideDown('fast');
        } else {
            $.jStorage.deleteKey("byteprint_" + $(this).prev().attr('id'));
            $(this).parent().next().slideUp('fast', function() {
                $(this).prev().addClass('closed');
            });
        }
    });
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

function CustomFileBrowser(field_name, url, type, win) {
    var cmsURL = "/admin/media/browse/?pop=2&tinymce=1";
    cmsURL = cmsURL + "&type=" + type;
    tinyMCE.activeEditor.windowManager.open({
        file: cmsURL,
        width: 815,  // Your dimensions may differ - toy around with them!
        height: 500,
        resizable: "yes",
        scrollbars: "yes",
        inline: "no",  // This parameter only has an effect if you use the inlinepopups plugin!
        close_previous: "no"
    }, {
        window: win,
        input: field_name,
        editor_id: tinyMCE.selectedInstance.editorId
    });
    return false;
}

function init_tinymce() {
    if ($('textarea.wysiwyg').length != 0) {
        $('textarea.wysiwyg').tinymce({
            script_url : '/static/core/admin/tiny_mce/tiny_mce.js',
            theme : "advanced",
            skin : "byteprint",
            plugins : "style,advimage,inlinepopups,media,contextmenu,visualchars,xhtmlxtras",
            //plugins : "style,advimage,inlinepopups,media,pdw,contextmenu,visualchars,xhtmlxtras",
            theme_advanced_buttons1 : "bold,italic,strikethrough,|,justifyleft,justifycenter,justifyright,|,bullist,numlist,|,link,unlink,|,image,|,code",
            // theme_advanced_buttons1 : "bold,italic,strikethrough,|,justifyleft,justifycenter,justifyright,|,bullist,numlist,|,link,unlink,|,image,|,code,|,pdw_toggle",
            theme_advanced_buttons2 : "underline,|,justifyfull,formatselect,forecolor,|,outdent,indent,|,media,charmap",
            theme_advanced_buttons3 : "",
            theme_advanced_buttons4 : "",
            theme_advanced_toolbar_location : "top",
            theme_advanced_toolbar_align : "left",
            theme_advanced_statusbar_location : "bottom",
            theme_advanced_resizing : true,
            file_browser_callback: "CustomFileBrowser",
            pdw_toggle_on : 1,
            pdw_toggle_toolbars : "2,3,4",
            height : '300',
            width : '586'
        });
    }
}

function init_msg() {
    $('.msg .icon').addClass('delete');
    $('.msg').live('click', function() {
        $(this).slideUp('fast');
    });
}