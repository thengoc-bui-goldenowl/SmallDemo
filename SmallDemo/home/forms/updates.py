from django import forms
from home.models import Dev, Project


class UpdateProjectForm(forms.ModelForm):
    dev = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': "autocomplete-dev",
            'id': "autocomplete-dev",
            'name': "autocomplete-dev"
        }))

    def __init__(self, *args, **kwargs):
        super(UpdateProjectForm, self).__init__(*args, **kwargs)


    class Meta:
        model = Project
        fields = ('name', 'des', 'start_date', 'end_date', 'cost', 'dev')
        labels = {
            'name': "Name",
            'des': "Description",
            'start_date': "Start Date",
            'end_date': "End Date",
            'dev': "Dev"

        }
        widgets = {
            'des': forms.Textarea
        }


class UpdateDevForm(forms.ModelForm):
    project = forms.CharField(required=False, widget=forms.TextInput(
        attrs={
            'class': "autocomplete-project",
            'id': "autocomplete-project",
            'name': "autocomplete-project"
        }))
    class Meta:
        model = Dev
        fields = ('first_name', 'last_name', 'language', 'active', 'project')
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "active": "State",
            "project": "project"
        }

class DetailDevForm(forms.ModelForm):
    class Meta:
        model = Dev
        fields = ('first_name', 'last_name', 'language', 'active')
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "active": "State",
        }

        
class DetailProjectForm(forms.ModelForm):
    class Meta:
        model= Project
        fields = ('name', 'des', 'start_date', 'end_date', 'cost')
        labels = {
            'name': "Name",
            'des': "Description",
            'start_date': "Start Date",
            'end_date': "End Date",
            'cost': "Cost"
        }