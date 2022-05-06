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
from home.views import *
from django.urls import path, include
from .models import *
from .serializers import *
# from rest_framework.routers import DefaultRouter
# router = DefaultRouter ()
# router.register('test', views.Test)

urlpatterns = [
     # path('test/', include(router.urls)),
    path('', Home.as_view(), name='home'),
    path('form/create/project/',
         CreateProject.as_view(), name='create_project'),
    path('form/create/dev/', CreateDev.as_view(), name='create_dev'),
    path('project/', ProjectPage.as_view(), name='project_page'),
     path('project/<int:project_id>/', UpdateProject.as_view(), name="project_update"),
    path('dev/', DevPage.as_view(), name='dev_page'),
    path('dev/<int:dev_id>/', UpdateDev.as_view(), name= "dev_update"),
    path('detail/dev/<int:dev_id>/', DetailDev.as_view(), name='detail_dev'),
    path('detail/project/<int:project_id>/', DetailProject.as_view(), name='detail_project'),
    path('form/devautocomplete/', DevAutocomplete.as_view(),
         name='dev_autocomplete'),
    path('form/projectautocomplete/', ProjectAutocomplete.as_view(),
         name='project_autocomplete'),
    path('search/project/name/', ProjectAutocomplete.as_view(),
         name='project_search_name_autocomplete'),
    path('search/project/name/<str:qry>/', SearchNameProject.as_view(),
         name='project_search_name'),
    path('search/project/date/<str:start_date>/<str:end_date>/', SearchDateProject.as_view(),
         name='project_search_date'),
    path('search/dev/name/', SearchNameDevAutocomplete.as_view(),
         name='dev_search_name_autocomplete'),
    path('search/dev/name/<str:qry>/', SearchNameDev.as_view(),
         name='dev_search_name'),   
    path('language/<str:lang>/', Language.as_view(), name="language"),
    path('paginateby/<int:count>/', CountDisplay.as_view(), name="count_display"),

]
