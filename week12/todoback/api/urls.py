from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('task_lists/', views.task_lists),
    path('task_lists/<int:pk>/', views.get_task_list),
    path('task_lists/<int:pk>/tasks/', views.get_task_list_tasks),
    path('tasks/<int:pk>/', views.get_task)
]
