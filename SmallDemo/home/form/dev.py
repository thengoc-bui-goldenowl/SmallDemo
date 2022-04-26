from django import forms
from home.models import Dev, Project



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