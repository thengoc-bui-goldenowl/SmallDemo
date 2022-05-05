
from django import forms
from home.models import Dev, Project
from django.utils.translation import gettext_lazy as _

class ProjectForm(forms.ModelForm):
    dev = forms.ModelChoiceField(queryset=Dev.objects.none())

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['dev'].queryset = Dev.objects.filter(active=True)

    class Meta:
        model = Project
        fields = ('name', 'des', 'start_date', 'end_date', 'cost', 'dev')
        labels = {
            'name': _("Name"),
            'des': _("Description"),
            'start_date': _("Start Date"),
            'end_date': _("End Date"),
            'dev': _("Dev"),

        }
