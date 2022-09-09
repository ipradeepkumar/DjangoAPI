from rest_framework import serializers
from api.models import Task


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('GUID','TotalIterations', 'Status')

