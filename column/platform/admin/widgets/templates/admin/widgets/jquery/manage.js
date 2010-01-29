function asyncWidgetAction(trigger) {
    var group = trigger.parent().parent().parent();
    $.post(trigger.attr('href'), function(refreshed_group) {
        group.html(refreshed_group);
    });
    return false;
}

$('a.icon.visible').live('click', function() {
    return asyncWidgetAction($(this));
});

$('a.icon.hidden').live('click', function() {
    return asyncWidgetAction($(this));
});

$('a.icon.down').live('click', function() {
    return asyncWidgetAction($(this));
});

$('a.icon.up').live('click', function() {
    return asyncWidgetAction($(this));
});

$('form#createWidgetForm').live('submit', function() {
    var groupBody = $('.groups_and_widgets ul:first');
    $.post(
        $(this).attr('action'),
        $(this).serialize(),
        function(refreshed_group_body) {
            groupBody.html(refreshed_group_body);
        }
    );
    return false;
});

$('form.groupRenameForm').live('submit', function() {
    var group_name = $(this).find('input[type=text]');
    $.post(
        $(this).attr('action'),
        $(this).serialize(),
        function(data) {
            $('p.msg').remove();
            group_name.val(data.name);
            var msg = '<p class="msg">' + data.msg + '<span class="right">'
            msg += '<span class="icon delete"></span></span></p>'
            $('h1:first').after(msg);
        },
        "json"
    );
    return false;
});