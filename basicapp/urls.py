from django.urls import path

from .views import *

urlpatterns = [
    path('hello/<name>',hello,name='hello'),
    path('timenow/',timenow, name='timenow'),
    path('show/',show,name='show'),
    path('staticcontent/',showstatic,name = 'showstatic'),
    path('showday/',showday,name='showday'),
    path('context/',contextview,name='contextview')
]
