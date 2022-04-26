from attr import field
from rest_framework import serializers
from home.models import Dev, Project


class DevSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dev
        fields = ('dev', 'first_name', 'last_name', 'active')


class ProjectSerializer(serializers.ModelSerializer):
    dev = DevSerializer(read_only=True, many=True)
    class Meta:
        model = Project
        fields = ('id', 'name', 'des', 'start_date', 'end_date','dev')
