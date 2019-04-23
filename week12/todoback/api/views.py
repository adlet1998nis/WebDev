from django.shortcuts import render
from django.http import JsonResponse
from api.models import TaskList, Task
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import TaskListSerializer, TaskSerializer
from datetime import datetime
# Create your views here.

@api_view(['GET', 'POST'])
def task_lists(request):
    if request.method == 'GET':
        lists = TaskList.objects.all()
        serializer = TaskListSerializer(lists, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TaskListSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def get_task_list(request, pk):
    try:
        list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return Response({
            'error': str(e)
        })

    if request.method == 'GET':
        serializer = TaskListSerializer(list)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskListSerializer(instance = list, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        list.delete()
        return Response({
            'list': 'deleted'
        })

@api_view(['GET', 'POST'])
def get_task_list_tasks(request, pk):
    try:
        tasks = Task.objects.filter(task_list = pk)
    except Task.DoesNotExist as e:
        return Response({
            'error': str(e)
        })

    if request.method == 'GET':
        serializer = TaskSerializer(tasks, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        task_list = TaskList.objects.get(id = pk)
        serializer = TaskSerializer(data = request.data)
        print(request.data)

        if serializer.is_valid():
            print("de")
            serializer.save(task_list = task_list)
            return Response(serializer.data)
        print(serializer.errors)
        return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def get_task(request, pk):
    try:
        task = Task.objects.get(id = pk)
    except Task.DoesNotExist as e:
        return Response({
            'error': str(e)
        })
    print(task)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    elif request.method == 'PUT':
        print(request.data)
        serializer = TaskSerializer(instance = task, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        task.delete()
        return Response({
            'task': 'deleted'
        })






