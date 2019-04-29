from django.contrib import admin
from django.urls import path
from api import views
from api.views import Task_lists, Get_task_list, Get_task_list_tasks, Get_task

urlpatterns = [
    path('task_lists/', Task_lists.as_view()),
    path('task_lists/<int:pk>/', Get_task_list.as_view()),
    path('task_lists/<int:pk>/tasks/', Get_task_list_tasks.as_view()),
    path('tasks/<int:pk>/', Get_task.as_view())
]
