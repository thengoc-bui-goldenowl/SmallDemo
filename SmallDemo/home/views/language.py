from django.shortcuts import render, HttpResponse, redirect
from http import HTTPStatus
from django.views import View
from django.http import QueryDict
from home.forms import ProjectForm, DevForm, UpdateProjectForm, UpdateDevForm, DetailDevForm, DetailProjectForm
#from home.serializers import DevSerializer, ProjectSerializer
from home.models import Dev, Project, ProjectDev
from django.http import JsonResponse
from datetime import datetime
from django.core.paginator import Paginator
from django.db.models import Q


class Language(View):

    def get(self, request, lang):
        if lang == request.COOKIES.get('currency'):
            response = JsonResponse(
                {'statusCode': '200', 'messages': 'Not Change'})
        else:
            response = JsonResponse(
                {'statusCode': '200', 'messages': 'Changing'})
            response.set_cookie('currency', lang)
        return response
