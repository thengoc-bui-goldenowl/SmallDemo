
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
