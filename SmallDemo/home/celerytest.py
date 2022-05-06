from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from home.tasks import *

def celery(request):
    res = add.delay()
    return HttpResponse(res.id)