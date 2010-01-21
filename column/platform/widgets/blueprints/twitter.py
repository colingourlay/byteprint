# from django import forms
# from platform.widgets import Blueprint
# import urllib2
# from django.utils import simplejson
# 
# class YQLTwitterBlueprint(Blueprint):
# 
#     name = 'yql-twitter'
#     display_name = 'YQL Twitter'
#     preview = True
#     fields = {
#         'username': forms.CharField(
#             required = False,
#             label = "Twitter User",
#             help_text = "Enter your Twitter username."
#         ),
#         'num_tweets': forms.IntegerField(
#             required = False,
#             label = "Number of Tweets",
#             help_text = "The number of tweets you want to be displayed inside \
#                 the widget. If you leave this blank, it will default to 1."
#         )
#     }
# 
#     def render(self, widget_data):
#         output = ""
#         if widget_data['username']:
#             num_tweets = 1
#             if widget_data['num_tweets']:
#                 num_tweets = widget_data['num_tweets']
#         result = urllib2.urlopen("http://query.yahooapis.com/v1/public/yql?q=select%20title%2Cabstract%20from%20search.web%20where%20query%3D%22colin%20gourlay%22&format=json").read()
#         data = simplejson.loads(result)
#         output += data['query']['results']['result'][0]['title']
#         return output
