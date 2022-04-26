from ntpath import join
from pkgutil import get_data
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.http import require_POST
from http import HTTPStatus
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView, RedirectView
from django.views import View
from matplotlib.pyplot import title
from home.forms import ProjectForm, DevForm, UpdateProjectForm, UpdateDevForm, DetailDevForm, DetailProjectForm
from home.serializers import DevSerializer, ProjectSerializer
from home.models import Dev, Project, ProjectDev
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from unittest import result
from datetime import datetime
from django.core import serializers
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.


class ContactListView(ListView):
    paginate_by = 2
    model = Project


def cover_data_project():
    data = Project.objects.values('id', 'name', 'des', 'start_date', 'end_date',
                                  'cost', 'dev__id', 'dev__first_name', 'dev__last_name').order_by('id')
    head = data[0]['id']
    data_cover = []
    data_cover.append([data[0]['id'], data[0]['name'], data[0]['des'],
                      data[0]['start_date'], data[0]['end_date'], data[0]['cost']])
    a = []
    count = 0
    for i in data:
        if i['id'] == head:
            a.append([i['dev__id'], i['dev__first_name'], i['dev__last_name']])
        else:
            head = i['id']
            data_cover[count].append(a)
            count = count+1
            data_cover.append([i['id'], i['name'], i['des'],
                              i['start_date'], i['end_date'], i['cost']])
            a = []
            a.append([i['dev__id'], i['dev__first_name'], i['dev__last_name']])
    data_cover[count].append(a)
    return data_cover


class Home(View):

    def get(self, request):

        return render(request, 'index.html', {'data': cover_data_project()})


class ProjectPage(View):

    def get(self, request):
        data = Project.objects.values('id', 'name', 'des', 'start_date', 'end_date',
                                      'cost').order_by('id')
        paginate_by = request.GET.get('paginate_by', 3)
        p = Paginator(data, paginate_by)
        page = request.GET.get('page', 1)
        page = p.page(page)
        data = page.object_list
        context = {'data': page, 'title_page': "List Project"}
        return render(request, 'project/projectpage.html', context)


class DevPage(View):

    def get(self, request):
        data = Dev.objects.values(
            'id', 'first_name', 'last_name', 'language', 'active').order_by('id')
        paginate_by = request.GET.get('paginate_by', 10)
        p = Paginator(data, paginate_by)
        page = request.GET.get('page', 1)
        page = p.page(page)
        data = page.object_list
        context = {'data': page, 'title_page': "List Dev"}
        return render(request, 'dev/devpage.html', context)


class CreateDev(View):

    def get(self, request):
        add_dev_form = DevForm()
        return render(request, 'popup.html', {'f': add_dev_form, 'index': 'create/dev', 'btn_class': 'creatDevSubmit', 'form_id': 'createDevForm', 'title_form': "New Dev"})

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
        except:
            response = JsonResponse({'statusCode': '500', 'message': "ERROR"},)
        return response


class CreateProject(View):

    def get(self, request):
        add_project_form = ProjectForm()
        return render(request, 'popup.html', {'f': add_project_form, 'index': 'create/project', 'btn_class': 'creatProjectSubmit', 'form_id': 'createProjectForm', 'title_form': "New Project"})

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
                dev_select = Dev.objects.get(id=dev_id)
                #dev_select.active = True
                # dev_select.save()
                new_project = Project(
                    des=des, name=name, start_date=start_date, end_date=end_date, cost=cost)
                new_project.save()
                new_project.dev.add(dev_select)
                new_project.save()
                project_dev = ProjectDev(
                    dev=dev_select, project=new_project, status=True)
                project_dev.save()
                response = JsonResponse(
                    {'statusCode': '200', 'message': "Successfully"})
            except Exception as err:
                response = JsonResponse(
                    {'statusCode': '500', 'message': "ERROR"},)
            return response


class UpdateProject(View):
    def get(self, request):
        project_id = request.GET.get('project_id')
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
        return render(request, 'project/updateproject.html', {'f': add_project_form, 'index': 'create/project', 'btn_class': 'creatProjectSubmit', 'form_id': 'createProjectForm', 'devs': dev, 'title_form': "Project Information"})

    def post(self, request):
        form = UpdateProjectForm(request.POST)
        if form.is_valid:
            try:
                request = request.POST
                print(request)
                project_id = des = request.get('project_id')
                des = request.get('des')
                name = request.get('name')
                start_date = request.get('start_date')
                end_date = request.get('end_date')
                cost = request.get('cost')
                devs = request.get('devs')

                project = Project.objects.get(id=project_id)
                devs_raw = project.dev.values('id')
                devs_raw = [i['id'] for i in devs_raw]
                devs = devs.split(',')[1:]
                devs = [int(i) for i in devs]
                devs_add = list(set(devs)-set(devs_raw))
                devs_remove = list(set(devs_raw)-set(devs))
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
            except Exception as err:
                response = JsonResponse(
                    {'statusCode': '500', 'message': "ERROR"},)
            return response


class RemoveProject(View):
    def post(self, request):

        project_id = request.POST.get('project_id')
        try:
            project = Project.objects.filter(id=project_id)
            project.delete()
            response = JsonResponse(
                {'statusCode': '200', 'messages': "Successfully"}
            )
        except:
            response = JsonResponse({
                'statusCode': '500'
            })
        return response


class RemoveDev(View):
    def post(self, request):

        dev_id = request.POST.get('dev_id')
        try:
            dev = Dev.objects.filter(id=dev_id)
            dev.delete()
            response = JsonResponse(
                {'statusCode': '200', 'messages': "Successfully"}
            )
        except:
            response = JsonResponse({
                'statusCode': '500'
            })
        return response


class UpdateDev(View):

    def get(self, request):
        dev_id = request.GET.get('dev_id')
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
        return render(request, 'dev/updatedev.html', {'f': add_dev_form, 'index': 'create/dev', 'btn_class': 'creatDevSubmit', 'form_id': 'createDevForm', 'projects': project, 'title_form': "Dev Information"})

    def post(self, request):
        try:
            dev_id = request.POST.get('dev_id')
            active = request.POST.get('active') == 'true'
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            language = request.POST.get('language')
            projects = request.POST.get('projects')
            dev = Dev.objects.get(id=dev_id)
            dev.first_name = first_name
            dev.last_name = last_name
            dev.language = language
            dev.active = active
            dev.save()
            projects = projects.split(',')[1:]
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
        except:
            response = JsonResponse({'statusCode': '500', 'message': "ERROR"},)
        return response


class DetailDev(View):

    def get(self, request):
        dev_id = request.GET.get('dev_id')
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
        return render(request, 'detail.html', {'f': add_dev_form, 'index': 'create/project', 'btn_class': 'creatProjectSubmit', 'form_id': 'createProjectForm', 'projects': project, 'title_form': "Dev Information"})


class DetailProject(View):

    def get(self, request):
        project_id = request.GET.get('project_id')
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
        return render(request, 'detail.html', {'f': add_project_form, 'index': 'create/project', 'btn_class': 'creatProjectSubmit', 'form_id': 'createProjectForm', 'projects': dev, 'title_form': "Project Information"})


class Pagination(View):

    def get(self, request):
        request = request.GET
        paginate_by = request.get('paginate_by')
        object = request.get('object')
        page = request.get('page')
        data = get_data()
        paginator = Paginator(data, 2)
        num_pages = paginator.num_pages
        page_number = request.GET.get('page')
        data = paginator.page(page_number).object_list
        page_obj = paginator.get_page(page_number)
        return render(request, 'dev/devtable.html', {'project': data, 'num_pages': num_pages, 'page_number': page_number})


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


class SearchDateProject(ProjectPage):

    def get(self, request):
        start_date = request.GET.get('startDate')
        end_date = request.GET.get('endDate')
        sd_date = datetime.strptime(start_date, '%Y-%m-%d')
        ed_date = datetime.strptime(end_date, '%Y-%m-%d')
        if sd_date > ed_date:
            start_date, end_date = end_date, start_date
        data = Project.objects.filter(Q(start_date__range=[start_date, end_date]) | Q(end_date__range=[start_date, end_date])).values('id', 'name', 'des', 'start_date', 'end_date',
                                                                                                                                      'cost')
        paginate_by = request.GET.get('paginate_by', 3)
        p = Paginator(data, paginate_by)
        page = request.GET.get('page', 1)
        page = p.page(page)
        data = page.object_list
        context = {'data': page}
        return render(request, 'project/projectpage.html', context)

class SearchNameDev(View):
    def get(self, request):
        qry = request.GET.get('term')
        data = Dev.objects.filter(
            Q(first_name__icontains=qry) | Q(last_name__icontains=qry))
        json = [str(i.id)+' - '+str(i) for i in data]
        return JsonResponse(json, safe=False)