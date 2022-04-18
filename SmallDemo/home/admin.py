from django.contrib import admin
from .models import Dev, ProjectManager, Project
# Register your models here.


class DevAdmin(admin.ModelAdmin):
    list_display=['id','first_name','last_name','active']
    list_filter =['id']
    search_fields=['id']

class ProjectAdmin(admin.ModelAdmin):
    list_display=['id','des','name','start_date','end_date']
    list_filter =['id']
    search_fields=['id']





class ProjectManagerAdmin(admin.ModelAdmin):
    list_display=['dev']
    list_filter =['dev']
    search_fields=['dev']
    @admin.display(empty_value='#')
    def id_pd(self, obj):
        return obj.dev


admin.site.register(ProjectManager, ProjectManagerAdmin)
admin.site.register(Dev, DevAdmin)
admin.site.register(Project, ProjectAdmin)
