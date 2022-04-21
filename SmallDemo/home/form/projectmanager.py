from django import forms
from home.models import ProjectManager

class ProjectManagerForm(forms.ModelForm):
    class Meta:
        model= ProjectManager
        fields=('id','project','dev',)