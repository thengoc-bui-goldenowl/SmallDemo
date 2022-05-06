from django import forms
from home.models import Dev, Project
from django.utils.translation import gettext_lazy as _

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
            'name': _("Name"),
            'des': _("Description"),
            'start_date': _("Start Date"),
            'end_date': _("End Date"),
            'dev': _("Dev"),
            'cost': _('Cost'),

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
            "first_name": _("First Name"),
            "last_name": _("Last Name"),
            "active": _("State"),
            "project": _("Project"),
            'language': _('Language'),
        }
