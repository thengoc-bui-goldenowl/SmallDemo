pass
from unittest import result
from django.shortcuts import render, HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from home.models import Dev, Project
from home.serializers import DevSerializer, ProjectSerializer
from home.forms import ProjectForm, DevForm
from django.views import View
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from http import HTTPStatus
from django.views.decorators.http import require_POST

# Create your views here.
class Home(View):

    def get(self, request):
        return render(request, 'index.html')


class CreateDev(View):

    def get(self, request):
        add_dev_form = DevForm()
        return render(request, 'popup.html',{'f':add_dev_form,'index':'create/dev', 'btn_class':'creatDevSubmit', 'form_id':'createDevForm'})

    def post(self, request):
        try:
            active=request.POST.get('active')=='true'
            first_name=request.POST.get('first_name')
            last_name=request.POST.get('last_name')
            language=request.POST.get('language')
            new_dev= Dev(first_name = first_name, last_name = last_name, language = language, active = active)
            new_dev.save()
            if active:
                project_id=request.POST.get('project')
                project=Project.objects.get(id=project_id)
                project.dev.add(new_dev)
            response = JsonResponse({'statusCode':'200','message':"Successfully"})   
        except:
            response =JsonResponse({'statusCode':'500','message':"ERROR"},)
        return response


class CreateProject(View):

    def get(self, request):
        add_project_form=ProjectForm()
        return render(request, 'popup.html',{'f':add_project_form, 'index':'create/project', 'btn_class':'creatProjectSubmit','form_id':'createProjectForm'})
    
    def post(self, request):
        form= ProjectForm(request.POST)
        if form.is_valid:
            try:
                request=request.POST
                des=request.get('des')
                name=request.get('name')
                start_date=request.get('start_date')
                end_date=request.get('end_date')
                cost=request.get('cost')
                dev_id=request.get('dev')
                dev_select=Dev.objects.get(id=dev_id)
                dev_select.active=True
                dev_select.save()
                new_project= Project(des = des, name = name, start_date = start_date, end_date = end_date, cost = cost)
                new_project.save()
                new_project.dev.add(dev_select)
                new_project.save()
                response = JsonResponse({'statusCode':'200','message':"Successfully"})
            except Exception as err:
                response =JsonResponse({'statusCode':'500','message':"ERROR"},)
            return response
            
       