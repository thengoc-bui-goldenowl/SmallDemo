
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


class SearchDateProject(View):

    def get(self, request, start_date, end_date):
        lang = request.COOKIES.get('lang') == 'vi'
        #start_date = request.GET.get('startDate')
        #end_date = request.GET.get('endDate')
        sd_date = datetime.strptime(start_date, '%Y-%m-%d')
        ed_date = datetime.strptime(end_date, '%Y-%m-%d')
        if sd_date > ed_date:
            start_date, end_date = end_date, start_date
        cache_key=str(start_date)+str(end_date)
        data = Project.objects.filter(Q(start_date__range=[start_date, end_date]) | Q(end_date__range=[start_date, end_date])).values('id', 'name', 'des', 'start_date', 'end_date',
                                                                                                                            'cost')
        paginate_by = request.GET.get('paginate_by', 3)
        p = Paginator(data, paginate_by)
        page = request.GET.get('page', 1)
        page = p.page(page)
        data = page.object_list
        context = {'data': page, 'lang': lang}
        return render(request, 'project/projectpage.html', context)


class SearchNameDev(View):
    def get(self, request):
        qry = request.GET.get('term')
        data = Dev.objects.filter(
            Q(first_name__icontains=qry) | Q(last_name__icontains=qry))
        json = [str(i.id)+' - '+str(i) for i in data]
        return JsonResponse(json, safe=False)
