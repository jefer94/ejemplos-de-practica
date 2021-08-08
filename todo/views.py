from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from todo.serializers import GetTaskSerializer, TaskSerializer
from todo.models import Task
from rest_framework.exceptions import APIException

class TaskView(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, task_id=None, task_slug=None):
        if task_id:
            elemento = Task.objects.filter(id=task_id).first()

            if not elemento:
                raise APIException('No existe este todo')

            serializer = GetTaskSerializer(elemento, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if task_slug:
            elemento = Task.objects.filter(slug=task_slug).first()

            if not elemento:
                raise APIException('No existe este todo')

            serializer = GetTaskSerializer(elemento, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elementos = Task.objects.all()
        serializer = GetTaskSerializer(elementos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
