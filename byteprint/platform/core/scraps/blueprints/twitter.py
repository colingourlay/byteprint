from django import forms

from platform.core.scraps import Blueprint

class TwitterBlueprint(Blueprint):

    name = 'twitter'
    display_name = 'Twitter'
    description = 'This Twitter scrap uses the official API javascript \
        interfece and will display a predetermined number of posts for any \
        specified user, provided they are in the Twitter pblic timeline.'
    preview = True
    fields = {
        'username': forms.CharField(
            required = False,
            label = "Twitter User",
            help_text = "Enter the name of the Twitter user who's timeline you \
                want to display. This must be a user who's tweets are in the \
                public timeline."
        ),
        'count': forms.IntegerField(
            required = False,
            label = "Number of Tweets",
            help_text = "Enter the number of tweets you want to be displayed. \
                If you leave this blank, it will default to 1."
        ),
        'ul_id': forms.CharField(
            required = True,
            label = "Output <ul id=\"?\">",
            help_text = "Tweets are written into your HTML as an unordered \
                list (between &lt;ul&gt; tags) with a unique id. In order to display \
                more than one scrap on a page, each will need a unique id.",
            initial = "twitter_update_list"
        )
    }

    def render(self, scrap_data):
        output = ""
        if scrap_data['username']:
            count = 1
            if scrap_data['count']:
                count = scrap_data['count']
            ul_id = "twitter_update_list"
            if scrap_data['ul_id']:
                ul_id = scrap_data['ul_id']
            output += "<ul id=\"" + ul_id + "\"><li>You need to have javascript enabled to view <a href=\"http://www.twitter.com/" + scrap_data['username'] + "/\">@" + scrap_data['username'] + "</a>'s Twitter status</li></ul>"
            output += """<script type=\"text/javascript\">function twitterCallback2(c){for(var b=[],a=0;a<c.length;a++){var e=c[a].user.screen_name,f=c[a].text.replace(/((https?|s?ftp|ssh)\:\/\/[^"\s\<\>]*[^.,;'">\:\s\<\>\)\]\!])/g,function(d){return'<a href="'+d+'">'+d+"</a>"}).replace(/\B@([_a-z0-9]+)/ig,function(d){return d.charAt(0)+'<a href="http://twitter.com/'+d.substring(1)+'">'+d.substring(1)+"</a>"});b.push("<li><span>"+f+'</span> <a style="font-size:85%" href="http://twitter.com/'+e+"/statuses/"+c[a].id+'">'+relative_time(c[a].created_at)+"</a></li>")}document.getElementById("""
            output += "\"" + ul_id + "\""
            output += """).innerHTML=b.join("")}function relative_time(c){var b=c.split(" ");c=b[1]+" "+b[2]+", "+b[5]+" "+b[3];var a=Date.parse(c);b=arguments.length>1?arguments[1]:new Date;a=parseInt((b.getTime()-a)/1E3);a+=b.getTimezoneOffset()*60;return a<60?"less than a minute ago":a<120?"about a minute ago":a<3600?parseInt(a/60).toString()+" minutes ago":a<7200?"about an hour ago":a<86400?"about "+parseInt(a/3600).toString()+" hours ago":a<172800?"1 day ago":parseInt(a/86400).toString()+" days ago"};</script>"""
            output += "<script type=\"text/javascript\" src=\"http://twitter.com/statuses/user_timeline/" + scrap_data['username'] + ".json?callback=twitterCallback2&count=" + count + "&&suppress_response_codes\"></script>"
            output += "<p><a href=\"http://www.twitter.com/" + scrap_data['username'] + "/\">Follow @" + scrap_data['username'] + " on Twitter</a></p>"
        return output
