from django.contrib import admin
from home.forms import ProjectForm, DevForm
from django import forms
from home.models import Project, Dev, ProjectDev
from django.db.models import OuterRef, Subquery
# Register your models here.


class DevAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'language', 'active']
    list_filter = ['language']
    search_fields = ['first_name', 'last_name']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'des', 'start_date', 'end_date', 'dev_name', 'cost']
    list_filter = ['name']
    search_fields = ['name']


class ProjectDevAdmin(admin.ModelAdmin):
    list_display = ['dev', 'project', 'date', 'status']
    list_filter = ['dev']
    search_fields = ['dev']


'''
class ProjectManagerInline(admin.TabularInline):
    model = ProjectManager.project.through

    
class ProjectManagerAdmin(admin.ModelAdmin):
    model = Project
    inlines = [
        ProjectManagerInline,
    ]
    list_display= ('id','dev','project_name')
    list_display_links = ('dev', 'project_name', )
    list_filter =['dev']
    search_fields=['dev']
   
admin.site.register(ProjectManager, ProjectManagerAdmin)
 '''
admin.site.register(Dev, DevAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectDev, ProjectDevAdmin)
