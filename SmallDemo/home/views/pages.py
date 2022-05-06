
from bdb import Breakpoint
from locale import currency
from socket import timeout
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
from django.utils.translation import get_language, activate


# Cover display full dev in project table----TEST


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


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class Home(View):

    def get(self, request):
        lang = request.COOKIES.get('lang') == 'vi'

        if cache.get("hello"):
            print("Data from cache")
            data = cache.get("hello")
        else:
            data = cover_data_project()
            cache.set("hello", data, timeout=60)
        title_page = _("Hello")
        context = {'data': data, 'lang': lang, 'title_page': title_page}
        response = render(request, 'index.html', context)
        # response.set_cookie('lang','en')
        return response


class ProjectPage(View):

    def get(self, request):
        lang = request.COOKIES.get('lang') == 'vi'
        currency = request.COOKIES.get('currency') == 'vnd'

        data = cache.get("project")
        if data:
            print("Data from cache")
        else:
            data = Project.objects.values('id', 'name', 'des', 'start_date', 'end_date',
                                          'cost').order_by('id')
            cache.set("project", data, timeout=60)
        paginate_by = request.COOKIES.get('count', 3)
        p = Paginator(data, paginate_by)
        page = request.GET.get('page', 1)
        page = p.page(page)
        data = page.object_list
        context = {'data': page, 'title_page': _(
            "List Project"), 'lang': lang, 'currency': currency, 'paginateby': paginate_by}
        return render(request, 'project/projectpage.html', context)


class DevPage(View):

    def get(self, request):
        lang = request.COOKIES.get('lang') == 'vi'
        currency = request.COOKIES.get('currency') == 'vnd'
        data = cache.get("dev")
        if data:
            print("Data from cache")
        else:
            data = Dev.objects.values(
                'id', 'first_name', 'last_name', 'language', 'active').order_by('id')
            cache.set("dev", data, timeout=60)

        paginate_by = request.COOKIES.get('count', 3)
        print("count", paginate_by)
        p = Paginator(data, paginate_by)
        page = request.GET.get('page', 1)
        page = p.page(page)
        data = page.object_list
        context = {'data': page, 'title_page': _(
            "List Dev"), 'currency': currency, 'lang': lang, 'paginateby': paginate_by}
        return render(request, 'dev/devpage.html', context)


class CountDisplay(View):

    def get(self, request, count):
        response = JsonResponse({'statusCode': '200'})
        response.set_cookie('count', count)
        return response
