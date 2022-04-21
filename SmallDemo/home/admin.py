from django.contrib import admin
from home.form.dev import DevForm
from home.form.project import ProjectForm
from home.form.projectmanager import ProjectManagerForm
from django import forms
from home.models import ProjectManager, Project, Dev
from django.db.models import OuterRef, Subquery
# Register your models here.


class DevAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','language','active']
    list_filter =['language']
    search_fields=['first_name','last_name']

class ProjectAdmin(admin.ModelAdmin):
    list_display=['des','name','start_date','end_date']
    list_filter =['name']
    search_fields=['name']
   

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
admin.site.register(Dev, DevAdmin)
admin.site.register(Project, ProjectAdmin)
