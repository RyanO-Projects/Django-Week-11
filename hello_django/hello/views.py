from django.http import HttpResponse
import re
from django.utils.timezone import datetime
from django.shortcuts import render

def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    print(request.build_absolute_uri())
    return render(
        request,
        'hello/hello_there.html',
        {
            'name' : name,
            'date' : datetime.now()
        }
    )
