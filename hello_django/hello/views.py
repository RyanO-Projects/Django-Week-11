from django.http import HttpResponse
import re
from django.utils.timezone import datetime

def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%a, %b %d, %Y at %X")

    # Filter the name argument o letters only using regular expressions.
    # URL arguments can contain arbitrary tent, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)