from unittest import result
from django.shortcuts import render, HttpResponse,redirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from home.models import Dev, Project, ProjectManager
from home.serializers import DevSerializer, ProjectSerializer, ProjectManagerSerializer
from .forms import DevForm, ProjectForm, ProjectManagerForm
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
            new_dev= Dev(first_name=first_name,last_name=last_name,active=active,language=language)
            new_dev.save()
            if active:
                project=request.POST.get('project')
                project_manager= ProjectManager(dev=new_dev)
                project_manager.save()
                project_manager.project.add(Project.objects.get(id=project))
            response = JsonResponse({'statusCode':'200','message':"Successfully"})   
        except:
            response =JsonResponse({'statusCode':'500','message':"ERROR"},)


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
                dev=Dev.objects.get(id=dev_id)
                dev.active=True
                dev.save()
                new_project= Project(des=des,name=name, start_date=start_date, end_date=end_date,cost=cost)
                new_project.save()
                project_manager= ProjectManager(dev=dev)
                project_manager.save()
                project_manager.project.add(new_project)
                project_manager.save()
                response = JsonResponse({'statusCode':'200','message':"Successfully"})
            except Exception as err:
                response =JsonResponse({'statusCode':'500','message':"ERROR"},)
            return response
            
       