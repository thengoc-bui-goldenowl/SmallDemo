from home.models import Dev, Project, ProjectDev
from rest_framework import serializers


class DevSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dev
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    dev = DevSerializer(read_only=True, many=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'des', 'start_date', 'end_date', 'cost' 'dev')
