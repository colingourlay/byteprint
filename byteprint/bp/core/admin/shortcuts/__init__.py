from django.http import HttpResponse
from django.utils import simplejson

def json_response(data):
    return HttpResponse(
        simplejson.dumps(data),
        mimetype='application/json'
    )