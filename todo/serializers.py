import serpy
from .models import Task
from rest_framework import serializers

class GetTaskSerializer(serpy.Serializer):
    id = serpy.Field()
    slug = serpy.Field()
    name = serpy.Field()
    description = serpy.Field()

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        exclude = ()