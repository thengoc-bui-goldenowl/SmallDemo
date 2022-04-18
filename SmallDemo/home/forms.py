from django import forms
from .models import Dev, Project, ProjectManager
import re
from django.core.exceptions import ObjectDoesNotExist

class DevForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.none())
   
    class Meta:
        model= Dev
        fields=('first_name','last_name','language','active','project')
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "active": "State",
            "project": "project"
        }

    def __init__(self, *args, **kwargs):
        super(DevForm,self).__init__(*args,**kwargs)
        self.fields['project'].queryset=Project.objects.all().distinct()
        self.fields['project'].disabled = True
        

    
class ProjectForm(forms.ModelForm, forms.Form):
    dev = forms.ModelChoiceField(queryset=Dev.objects.none())
    def __init__(self, *args, **kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)
        self.fields['dev'].queryset=Dev.objects.filter(active=False)
    class Meta:
        model= Project
        fields=('name','des','start_date','end_date','cost','dev')
        labels = {
            'name': "Name",
            'des': "Description",
            'start_date': "Start Date",
            'end_date': "End Date",
            'dev': "Dev"

        }
        
class ProjectManagerForm(forms.ModelForm):
    class Meta:
        model= ProjectManager
        fields=('id','project','dev',)
    
class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass