from django.shortcuts import render
from django.http import JsonResponse
from api.models import TaskList, Task
# Create your views here.

def task_lists(request):
    t_lists = TaskList.objects.all()
    json_t_lists = [t.to_json() for t in t_lists]
    return JsonResponse(json_t_lists, safe = False)

def get_task_list(request, pk):
    try:
        task_list = TaskList.objects.get(id = pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(task_list.to_json())

def get_task_list_tasks(request, pk):
    tasks = Task.objects.filter(task_list = pk)
    json_tasks = [t.to_json_for_c() for t in tasks]
    return JsonResponse(json_tasks, safe = False)

def get_task(request, pk):
    try:
        task = Task.objects.get(id = pk)
    except Task.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(task.to_json_for_d())




