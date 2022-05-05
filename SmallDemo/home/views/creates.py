
from functools import cache
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
from django.core.cache import cache
from django.conf import settings
from django.utils.translation import gettext as _


class CreateDev(View):

    def get(self, request):
        add_dev_form = DevForm()
        return render(request, 'popup.html', {'f': add_dev_form, 'index': 'create/dev', 'btn_class': 'creatDevSubmit', 'form_id': 'createDevForm', 'title_form': _("New Dev")})

    def post(self, request):
        try:
            active = request.POST.get('active') == 'true'
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            language = request.POST.get('language')
            new_dev = Dev(first_name=first_name, last_name=last_name,
                          language=language, active=active)
            new_dev.save()
            if active:
                project_id = request.POST.get('project')
                project = Project.objects.get(id=project_id)
                project.dev.add(new_dev)
                project.save()
                project_dev = ProjectDev(
                    dev=new_dev, project=project, status=True)
                project_dev.save()
            response = JsonResponse(
                {'statusCode': '200', 'message': "Successfully"})
            cache.set("dev", "")
        except:
            response = JsonResponse({'statusCode': '500', 'message': "ERROR"},)
        return response


class CreateProject(View):

    def get(self, request):
        add_project_form = ProjectForm()
        return render(request, 'popup.html', {'f': add_project_form, 'index': 'create/project', 'btn_class': 'creatProjectSubmit', 'form_id': 'createProjectForm', 'title_form': _("New Project")})

    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid:
            try:
                request = request.POST
                des = request.get('des')
                name = request.get('name')
                start_date = request.get('start_date')
                end_date = request.get('end_date')
                cost = request.get('cost')
                dev_id = request.get('dev')
                #dev_select.active = True
                # dev_select.save()
                new_project = Project(
                    des=des, name=name, start_date=start_date, end_date=end_date, cost=cost)
                new_project.save()
                try:
                    dev_select = Dev.objects.get(id=dev_id)
                    new_project.dev.add(dev_select)
                    new_project.save()
                    project_dev = ProjectDev(
                        dev=dev_select, project=new_project, status=True)
                    project_dev.save()
                except:
                    pass
                response = JsonResponse(
                    {'statusCode': '200', 'message': "Successfully"})
                cache.set("project", "")
            except Exception as err:
                response = JsonResponse(
                    {'statusCode': '500', 'message': "ERROR"},)
            return response
