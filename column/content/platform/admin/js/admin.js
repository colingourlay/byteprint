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
        tinyMCE.init({
            "spellchecker_languages": "Arabic=ar,Bulgarian=bg,Bengali / Bosnian=bn,Catalan=ca,Czech=cs,Welsh=cy,Danish=da,German=de,Greek=el,+English=en,Spanish / Argentinean Spanish=es,Estonian=et,Basque=eu,Persian=fa,Finnish=fi,French=fr,Frisian=fy,Irish=ga,Galician=gl,Hebrew=he,Hindi=hi,Croatian=hr,Hungarian=hu,Icelandic=is,Italian=it,Japanese=ja,Georgian=ka,Khmer=km,Kannada=kn,Korean=ko,Lithuanian=lt,Latvian=lv,Macedonian=mk,Dutch=nl,Norwegian=no,Polish=pl,Portuguese / Brazilian Portuguese=pt,Romanian=ro,Russian=ru,Slovak=sk,Slovenian=sl,Albanian=sq,Serbian / Serbian Latin=sr,Swedish=sv,Tamil=ta,Telugu=te,Thai=th,Turkish=tr,Ukrainian=uk,Simplified Chinese / Traditional Chinese=zh",
            "elements": "id_content",
            "language": "en",
            "directionality": "ltr",
            "theme": "advanced",
            "strict_loading_mode": 1,
            "mode": "exact",
            "skin": "o2k7",
            "height": 350
        })
    }
}

function init_msg() {
    $('.msg .icon').addClass('delete');
    $('.msg').live('click', function() {
        $(this).slideUp('fast');
    });
}