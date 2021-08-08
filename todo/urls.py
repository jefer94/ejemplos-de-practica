from django.urls import path
from .views import (TaskView)

app_name = 'todo'
urlpatterns = [
    path('tarea', TaskView.as_view()),
    path('tarea/<int:task_id>/', TaskView.as_view()),
    path('tarea/<str:task_slug>/', TaskView.as_view()),
]
