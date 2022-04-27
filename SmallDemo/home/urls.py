"""SmallDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from .views import views
from django.urls import path, include
from .models import *
from .serializers import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter ()
router.register('test', views.Test)

urlpatterns = [
     path('test/', include(router.urls)),
    path('', views.Home.as_view(), name='home'),
    
    path('form/create/project/',
         views.CreateProject.as_view(), name='create_project'),
    path('form/create/dev/', views.CreateDev.as_view(), name='create_dev'),
    path('project/', views.ProjectPage.as_view(), name='project_page'),
     path('project/<int:project_id>/', views.UpdateProject.as_view(), name="project_update"),
    path('dev/', views.DevPage.as_view(), name='dev_page'),
    path('dev/<int:dev_id>/', views.UpdateDev.as_view(), name= "dev_update"),
    path('form/detail/dev/', views.DetailDev.as_view(), name='detail_dev'),
    path('form/detail/project/', views.DetailProject.as_view(), name='detail_project'),
    path('form/devautocomplete/', views.DevAutocomplete.as_view(),
         name='dev_autocomplete'),
    path('form/projectautocomplete/', views.ProjectAutocomplete.as_view(),
         name='project_autocomplete'),
    path('search/project/name/', views.ProjectAutocomplete.as_view(),
         name='project_search_name'),
    path('search/project/date/', views.SearchDateProject.as_view(),
         name='project_search_date'),
    path('search/dev/name/', views.SearchNameDev.as_view(),
         name='dev_search_name'),
]
