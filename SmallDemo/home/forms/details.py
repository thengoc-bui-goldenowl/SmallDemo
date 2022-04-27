from django import forms
from home.models import Dev, Project


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
        model = Project
        fields = ('name', 'des', 'start_date', 'end_date', 'cost')
        labels = {
            'name': "Name",
            'des': "Description",
            'start_date': "Start Date",
            'end_date': "End Date",
            'cost': "Cost"
        }
