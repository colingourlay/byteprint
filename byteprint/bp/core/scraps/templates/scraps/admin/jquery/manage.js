function asyncPileToggle(trigger) {
    var pile_header = trigger.parent().parent();
    $.post(trigger.attr('href'), function(refreshed_pile_header) {
        pile_header.replaceWith(refreshed_pile_header);
    });
    return false;
}

$('.pile_header a.icon.visible').live('click', function() {
    return asyncPileToggle($(this));
});

$('.pile_header a.icon.hidden').live('click', function() {
    return asyncPileToggle($(this));
});

function asyncScrapRepositionOrToggle(trigger) {
    var pileBody = trigger.parent().parent().parent().parent();
    $.post(trigger.attr('href'), function(refreshed_pile_body) {
        pileBody.html(refreshed_pile_body);
    });
    return false;
}

$('.pane_list_item a.icon.visible').live('click', function() {
    return asyncScrapRepositionOrToggle($(this));
});

$('.pane_list_item a.icon.hidden').live('click', function() {
    return asyncScrapRepositionOrToggle($(this));
});

$('.pane_list_item a.icon.down').live('click', function() {
    return asyncScrapRepositionOrToggle($(this));
});

$('.pane_list_item a.icon.up').live('click', function() {
    return asyncScrapRepositionOrToggle($(this));
});

function asyncPileDeleteOrScrapRepileOrDelete(trigger) {
    var allPiles = $('#all_piles');
    $.post(trigger.attr('href'), function(refreshed_all_piles) {
        allPiles.empty().append(refreshed_all_piles);
    });
    return false;
}

$('.pile_header a.icon.pileDelete').live('click', function() {
    return asyncPileDeleteOrScrapRepileOrDelete($(this));
});

$('.pane_list_item a.icon.scrapDelete').live('click', function() {
    return asyncPileDeleteOrScrapRepileOrDelete($(this));
});

$('.pane_list_item a.scrap_repile').live('click', function() {
    return asyncPileDeleteOrScrapRepileOrDelete($(this));
});

$('form#createScrapForm').live('submit', function() {
    var unpileedBody = $('#unpiled_body');
    $.post(
        $(this).attr('action'),
        $(this).serialize(),
        function(refreshed_pile_body) {
            unpileedBody.empty().append(refreshed_pile_body);
        }
    );
    return false;
});

$('form#createPileForm').live('submit', function() {
    var allpiles = $('#all_piles');
    $.post(
        $(this).attr('action'),
        $(this).serialize(),
        function(refreshed_all_piles) {
            allpiles.empty().append(refreshed_all_piles);
        }
    );
    return false;
});

$('form.pileRenameForm').live('submit', function() {
    var pile_name = $(this).find('input[type=text]');
    $.post(
        $(this).attr('action'),
        $(this).serialize(),
        function(data) {
            $('p.msg').remove();
            pile_name.val(data.name);
            var msg = '<p class="msg">' + data.msg + '<span class="right">';
            msg += '<span class="icon delete"></span></span></p>';
            $('h1:first').after(msg);
        },
        "json"
    );
    return false;
});