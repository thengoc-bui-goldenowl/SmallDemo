from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from home.tasks import *

class Celerytest(View):

    def get(self, request):
        res = add.delay(3,4)
        return HttpResponse("Done")