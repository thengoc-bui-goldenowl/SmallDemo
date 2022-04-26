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
from torch import view_as_real
from . import views
from django.urls import path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('form/create/project/',
         views.CreateProject.as_view(), name='create_project'),
    path('form/create/dev/', views.CreateDev.as_view(), name='create_dev'),
    path('project/', views.ProjectPage.as_view(), name='project_page'),
    path('dev/', views.DevPage.as_view(), name='dev_page'),
    path('form/update/project/',
         views.UpdateProject.as_view(), name='update_project'),
    path('form/update/dev/', views.UpdateDev.as_view(), name='update_dev'),
    path('form/detail/dev/', views.DetailDev.as_view(), name='detail_dev'),
    path('form/detail/project/', views.DetailProject.as_view(), name='detail_dev'),
    path('form/devautocomplete/', views.DevAutocomplete.as_view(),
         name='dev_autocomplete'),
    path('form/projectautocomplete/', views.ProjectAutocomplete.as_view(),
         name='project_autocomplete'),
    path('form/remove/project/',
         views.RemoveProject.as_view(), name='remove_project'),
    path('form/remove/dev/',
         views.RemoveDev.as_view(), name='remove_project'),
    path('search/project/name/', views.ProjectAutocomplete.as_view(),
         name='project_search_name'),
    path('search/project/date/', views.SearchDateProject.as_view(),
         name='project_search_date'),
    path('search/dev/name/', views.SearchNameDev.as_view(),
         name='dev_search_name'),
]
