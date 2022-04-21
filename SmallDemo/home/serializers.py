from attr import field
from rest_framework import serializers
from home.models import Dev, Project

class DevSerializer(serializers.ModelSerializer):
    class Meta:
        model= Dev
        field=('dev','first_name','last_name','active')
    
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        field=('id','name','des','start_date','end_date')


    
