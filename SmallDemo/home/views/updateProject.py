
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
    cache.set("project","")

class UpdateProject(View):
    def get(self, request, project_id):
        #project_id = request.GET.get('project_id')
        project = Project.objects.get(id=project_id)
        des = project.des
        name = project.name
        start_date = project.start_date
        end_date = project.end_date
        cost = project.cost
        dev = Dev.objects.filter(project__id=project_id)
        dev = [[_.id, str(_)] for _ in dev]
        print(dev)
        add_project_form = UpdateProjectForm(initial={'des': des, 'name': name,
                                                      'start_date': start_date, 'end_date': end_date, 'cost': cost,
                                                      })
        return render(request, 'project/updateproject.html', {'f': add_project_form, 'index': 'create/project', 'btn_class': 'creatProjectSubmit', 'form_id': 'createProjectForm', 'devs': dev, 'title_form': _("Project Information")})

    def patch(self, request, project_id):
        data=json.loads(request.body)
        form = UpdateProjectForm(data)
        if form.is_valid:   
            try:
                des = data['des']
                name = data['name']
                start_date = data['start_date']
                end_date = data['end_date']
                cost = data['cost']
                devs = data['devs']
                project = Project.objects.get(id=project_id)
                try:
                    devs_raw = project.dev.values('id')
                    devs_raw = [i['id'] for i in devs_raw]
                    devs = devs.split(',')[1:]
                    devs = [int(i) for i in devs]
                    devs_add = list(set(devs)-set(devs_raw))
                    devs_remove = list(set(devs_raw)-set(devs))
                    print("devs",devs)
                    for dev_id in devs_add:
                        dev_select = Dev.objects.get(id=dev_id)
                        project.dev.add(dev_select)
                        project.save()
                        project_dev = ProjectDev(
                            dev=dev_select, project=project, status=True)
                        project_dev.save()
                    for dev_id in devs_remove:
                        dev_select = Dev.objects.get(id=dev_id)
                        project.dev.remove(dev_select)
                        project_dev = ProjectDev(
                            dev=dev_select, project=project, status=False)
                        project_dev.save()
                except:
                    pass
                project.name = name
                project.des = des
                project.start_date = start_date
                project.end_date = end_date
                project.cost = cost
                project.save()
                
                #dev_select.active = True
                # dev_select.save()
                response = JsonResponse(
                    {'statusCode': '200', 'message': "Successfully"})
                remove_cache()
            except Exception as err:
                response = JsonResponse(
                    {'statusCode': '500', 'message': "ERROR"},)
            return response

    def delete(self, request, project_id):
        try:
            project = Project.objects.filter(id=project_id)
            project.delete()
            response = JsonResponse(
                {'statusCode': '200', 'messages': "Successfully"}
            )
            remove_cache()
        except:
            response = JsonResponse({
                'statusCode': '500'
            })
        return response
