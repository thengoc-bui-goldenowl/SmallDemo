
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
import json


def remove_cache():
    cache.set("dev", "")


class UpdateDev(View):

    def get(self, request, dev_id):
        #dev_id = request.GET.get('dev_id')
        dev = Dev.objects.get(id=dev_id)
        first_name = dev.first_name
        last_name = dev.last_name
        active = dev.active
        language = dev.language
        project = Project.objects.filter(dev__id=dev_id)
        project = [[i.id, str(i)] for i in project]

        add_dev_form = UpdateDevForm(initial={'first_name': first_name, 'last_name': last_name,
                                              'active': active, 'language': language,

                                              })
        return render(request, 'dev/updatedev.html', {'f': add_dev_form, 'index': 'create/dev', 'btn_class': 'creatDevSubmit', 'form_id': 'createDevForm', 'projects': project, 'title_form': _("Dev Information")})

    def patch(self, request, dev_id):
        data=json.loads(request.body)
        
        try:
            #dev_id = request.POST.get('dev_id')
            active = data['active'] == 'true'
            first_name = data['first_name']
            last_name = data['last_name']
            language = data['language']
            projects = data['projects']
            dev = Dev.objects.get(id=dev_id)
            dev.first_name = first_name
            dev.last_name = last_name
            dev.language = language
            dev.active = active
            dev.save()
            projects = projects.split(',')[1:]
            if projects:
                projects = [int(i) for i in projects]
                projects_raw = Project.objects.filter(dev__id=dev_id).values('id')
                projects_raw = [i['id'] for i in projects_raw]
                # add
                project_add = list(set(projects)-set(projects_raw))
                # remove
                project_remove = list(set(projects_raw)-set(projects))
                for p in project_add:
                    project = Project.objects.get(id=p)
                    project.dev.add(dev)
                    project.save()
                    project_dev = ProjectDev(
                        dev=dev, project=project, status=True)
                    project_dev.save()

                for p in project_remove:
                    project = Project.objects.get(id=p)
                    project.dev.remove(dev)
                    project.save()
                    project_dev = ProjectDev(
                        dev=dev, project=project, status=False)
                    project_dev.save()
            response = JsonResponse(
                {'statusCode': '200', 'message': "Successfully"})
            remove_cache()

        except:
            response = JsonResponse({'statusCode': '500', 'message': "ERROR"},)
        return response

    def delete(self, request, dev_id):

        try:
            dev = Dev.objects.filter(id=dev_id)
            dev.delete()
            response = JsonResponse(
                {'statusCode': '200', 'messages': "Successfully"}
            )
            remove_cache()
        except:
            response = JsonResponse({
                'statusCode': '500'
            })
        return response
