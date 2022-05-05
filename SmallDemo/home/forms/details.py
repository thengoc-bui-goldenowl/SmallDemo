from django import forms
from home.models import Dev, Project
from django.utils.translation import gettext_lazy as _

class DetailDevForm(forms.ModelForm):
    class Meta:
        model = Dev
        fields = ('first_name', 'last_name', 'language', 'active')
        labels = {
            "first_name": _("First Name"),
            "last_name": _("Last Name"),
            "active": _("State"),
            'language': _("Language"),
        }


class DetailProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'des', 'start_date', 'end_date', 'cost')
        labels = {
            'name': _("Name"),
            'des': _("Description"),
            'start_date': _("Start Date"),
            'end_date': _("End Date"),
            'cost': _("Cost"),
        }
