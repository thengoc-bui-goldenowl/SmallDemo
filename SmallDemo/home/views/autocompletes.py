
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


class DevAutocomplete(View):
    def get(self, request):
        qry = request.GET.get('term')
        data = Dev.objects.filter(
            Q(first_name__icontains=qry) | Q(last_name__icontains=qry)).filter(active=True)
        json = [str(i.id)+' - '+str(i) for i in data]
        return JsonResponse(json, safe=False)


class ProjectAutocomplete(View):
    def get(self, request):
        qry = request.GET.get('term')
        data = Project.objects.filter(name__icontains=qry)
        json = [str(i.id)+' - '+str(i) for i in data]
        return JsonResponse(json, safe=False)
