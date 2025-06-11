from django.shortcuts import render

from django.http import request
from django.http import *
from django.views.decorators.http import require_http_methods
from django.template import loader

import datetime

# Create your views here.

def hello(request , name):
    if name == 'jayanth':

        return HttpResponse('<h1>hello %s</h1>' %(name))
    
    else:

        return HttpResponseNotFound('<h1>Page not found</h1>')



def timenow(request):
    template = loader.get_template('time.html')
    return HttpResponse(template.render())

@require_http_methods(['GET'])
def show(request):
    return HttpResponse("This is a aGET request")

def showstatic(request):
    template = loader.get_template('static.html')
    return HttpResponse(template.render())

def showday(request):
    return render(request,'Day.html',{'today':datetime.datetime.now().month})

def contextview(request):
    template = loader.get_template('context.html')
    context = {'name':'Jayanth'}
    return HttpResponse(template.render(context,request))
    