from django import forms
from platform.core.widgets import Blueprint

class TwitterBlueprint(Blueprint):

    name = 'twitter'
    display_name = 'Twitter'
    preview = True
    fields = {
        'username': forms.CharField(
            required = False,
            label = "Twitter User",
            help_text = "Enter the name of the Twitter user who's timeline you \
                want to display."
        ),
        'count': forms.IntegerField(
            required = False,
            label = "Number of Tweets",
            help_text = "Enter the number of tweets you want to be displayed. \
                If you leave this blank, it will default to 1."
        )
    }

    def render(self, widget_data):
        output = ""
        if widget_data['username']:
            count = 1
            if widget_data['count']:
                count = widget_data['count']
                output += "<p><a href=\"http://www.twitter.com/" + widget_data['username'] + "/\">Follow @" + widget_data['username'] + " on Twitter</a></p>"
            output += "<ul id=\"twitter_update_list\"><li>You need to have javascript enabled to view <a href=\"http://www.twitter.com/" + widget_data['username'] + "/\">@" + widget_data['username'] + "</a>'s Twitter status</li></ul>"
            output += "<script type=\"text/javascript\" src=\"http://twitter.com/javascripts/blogger.js\"></script>"    
            output += "<script type=\"text/javascript\" src=\"http://twitter.com/statuses/user_timeline/" + widget_data['username'] + ".json?callback=twitterCallback2&count=" + count + "\"></script>"
            print output
        return output
