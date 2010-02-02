function asyncGroupAction(trigger) {
    var group_header = trigger.parent().parent();
    $.post(trigger.attr('href'), function(refreshed_group_header) {
        group_header.replaceWith(refreshed_group_header);
    });
    return false;
}

$('.group_header a.icon.visible').live('click', function() {
    return asyncGroupAction($(this));
});

$('.group_header a.icon.hidden').live('click', function() {
    return asyncGroupAction($(this));
});

function asyncWidgetRepositionOrToggle(trigger) {
    var groupBody = trigger.parent().parent().parent().parent();
    $.post(trigger.attr('href'), function(refreshed_group_body) {
        groupBody.html(refreshed_group_body);
    });
    return false;
}

$('.widget_list_item a.icon.visible').live('click', function() {
    return asyncWidgetRepositionOrToggle($(this));
});

$('.widget_list_item a.icon.hidden').live('click', function() {
    return asyncWidgetRepositionOrToggle($(this));
});

$('.widget_list_item a.icon.down').live('click', function() {
    return asyncWidgetRepositionOrToggle($(this));
});

$('.widget_list_item a.icon.up').live('click', function() {
    return asyncWidgetRepositionOrToggle($(this));
});

function asyncGroupDeleteOrWidgetRegroupOrDelete(trigger) {
    var allGroups = $('#all_groups');
    $.post(trigger.attr('href'), function(refreshed_all_groups) {
        allGroups.empty().append(refreshed_all_groups);
    });
    return false;
}

$('.group_header a.icon.groupDelete').live('click', function() {
    return asyncGroupDeleteOrWidgetRegroupOrDelete($(this));
});

$('.widget_list_item a.icon.widgetDelete').live('click', function() {
    return asyncGroupDeleteOrWidgetRegroupOrDelete($(this));
});

$('.widget_list_item a.widget_regroup').live('click', function() {
    return asyncGroupDeleteOrWidgetRegroupOrDelete($(this));
});

$('form#createWidgetForm').live('submit', function() {
    var ungroupedBody = $('#ungrouped_body');
    $.post(
        $(this).attr('action'),
        $(this).serialize(),
        function(refreshed_group_body) {
            ungroupedBody.empty().append(refreshed_group_body);
        }
    );
    return false;
});

$('form#createGroupForm').live('submit', function() {
    var allGroups = $('#all_groups');
    $.post(
        $(this).attr('action'),
        $(this).serialize(),
        function(refreshed_all_groups) {
            allGroups.empty().append(refreshed_all_groups);
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