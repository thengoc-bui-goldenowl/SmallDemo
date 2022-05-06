
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
from django.utils.translation import gettext as _


class DetailDev(View):

    def get(self, request,dev_id):
        #dev_id = request.GET.get('dev_id')
        dev = Dev.objects.get(id=dev_id)
        first_name = dev.first_name
        last_name = dev.last_name
        active = dev.active
        language = dev.language
        project = Project.objects.filter(dev__id=dev_id)
        project = [[_.id, str(_)] for _ in project]

        add_dev_form = DetailDevForm(initial={'first_name': first_name, 'last_name': last_name,
                                              'active': active, 'language': language,

                                              })
        for field in add_dev_form.fields:
            add_dev_form.fields[field].disabled = True
        return render(request, 'detail.html', {'f': add_dev_form, 'index': 'create/project', 'btn_class': 'creatProjectSubmit', 'form_id': 'createProjectForm', 'projects': project, 'title_form': _("Dev Information")})


class DetailProject(View):

    def get(self, request, project_id):
        #project_id = request.GET.get('project_id')
        project = Project.objects.get(id=project_id)
        name = project.name
        des = project.des
        start_date = project.start_date
        end_date = project.end_date
        cost = project.cost
        dev = Dev.objects.filter(project__id=project_id)
        dev = [[i.id, str(i)] for i in dev]

        add_project_form = DetailProjectForm(initial={'name': name, 'des': des,
                                                      'start_date': start_date, 'end_date': end_date,
                                                      'cost': cost

                                                      })
        for field in add_project_form.fields:
            add_project_form.fields[field].disabled = True
        return render(request, 'detail.html', {'f': add_project_form, 'index': 'create/project', 'btn_class': 'creatProjectSubmit', 'form_id': 'createProjectForm', 'projects': dev, 'title_form': _("Project Information")})
