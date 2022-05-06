from django import forms
from home.models import Dev, Project
from django.utils.translation import gettext_lazy as _



class DevForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.none())

    class Meta:
        model = Dev
        fields = ('first_name', 'last_name', 'language', 'active', 'project')
        labels = {
            "first_name": _("First Name"),
            "last_name": _("Last Name"),
            "active": _("State"),
            "project": _("project"),
            'language': _('language')
        }

    def __init__(self, *args, **kwargs):
        super(DevForm, self).__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.all().distinct()
        self.fields['project'].disabled = True
