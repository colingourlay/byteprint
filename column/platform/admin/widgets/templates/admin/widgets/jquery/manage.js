function async(trigger) {
    var group = trigger.parent().parent().parent();
    $.post(trigger.attr('href'), function(refreshed_group) {
        group.html(refreshed_group);
    });
    return false;
}

$('a.icon.visible').live('click', function() {
    return async($(this));
});

$('a.icon.hidden').live('click', function() {
    return async($(this));
});

// $('a.icon.down').live('click', function() {
//     return async($(this));
// });
// 
// $('a.icon.up').live('click', function() {
//     return async($(this));
// });