from django import forms
from platform.widgets import Blueprint

# from platform.widgets.dependencies import twitter

# class TwitterBlueprint(Blueprint):
# 
#     name = 'twitter'
#     display_name = 'Twitter Timeline'
#     preview = True
#     fields = {
#         'username': forms.CharField(
#             required = False,
#             label = "Twitter Username",
#             help_text = "Enter your Twitter username. This will be used to \
#                 retrieve your latest Twitter status."
#         ),
#         'password': forms.CharField(
#             required = False,
#             label = "Twitter Password",
#             help_text = "Your password is needed to authenticate your Twitter \
#                 API requests.",
#             widget = forms.PasswordInput()
#         ),
#         'num_tweets': forms.IntegerField(
#             required = False,
#             label = "Number of Tweets",
#             help_text = "The number of tweets you want to be displayed inside \
#                 the widget. If you leave this blank, the widget will display \
#                 only your latest tweet."
#         )
#     }
# 
#     def render(self, widget_data):
#         output = ""
#         if widget_data['username']:
#             api = twitter.Api(widget_data['username'], widget_data['password'])
#             try:
#                 tweets = api.GetUserTimeline(widget_data['username'])
#             except Exception, e:
#                 return "<!-- Twitter API connection error -->"
#             num_tweets = 1
#             if widget_data['num_tweets']:
#                 num_tweets = int(widget_data['num_tweets'])
#             output += "<dl class=\"twitter_timeline\">"
#             tweets = tweets[:num_tweets]
#             for tweet in tweets:
#                 text = re.sub(r'http://([\w\./-]+)', r'<a href="http://\1">http://\1</a>', tweet.text)
#                 text = re.sub(r'@(\w+)', r'<a href="http://www.twitter.com/\1">@\1</a>', text)
#                 text = re.sub(r'#(\w+)', r'<a href="http://search.twitter.com/search?q=\1">#\1</a>', text)
#                 output += "<dt>" + text + "</dt>"
#                 output += "<dd>" + tweet.relative_created_at + "</dd>"
#             output += "</dl>"
#         return output