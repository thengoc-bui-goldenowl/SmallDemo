
from django import forms
from home.models import Dev, Project


class ProjectForm(forms.ModelForm):
    dev = forms.ModelChoiceField(queryset=Dev.objects.none())

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['dev'].queryset = Dev.objects.filter(active=True)

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
