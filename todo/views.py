from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status
from .models import Todo
from .serializers import TodoSerializer
from .filters import ProductFilter
from django_filters.utils import translate_validation
from django.db.models import F

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def TodoList(request):

    if request.method == 'GET':
        todos = Todo.objects.all()
        filterset = ProductFilter(request.GET, queryset=todos)
        if not filterset.is_valid():
            raise translate_validation(filterset.errors)
        serializer = TodoSerializer(filterset.qs, many=True)

        # Sorting feature
        # First check is the para of 'sort_by' is appear
        sort_by = request.query_params.get('sort_by')
        if sort_by:
        # Split sorting parameters by comma
            sort_params = sort_by.split(',')
        # Apply sorting to the queryset based on the sorting parameters
            for param in sort_params:
                if param.startswith('-'):
                    todos = todos.order_by(F(param[1:]).desc(nulls_last=True))
                else:
                    todos = todos.order_by(F(param).asc(nulls_last=True))
            serializer = TodoSerializer(todos, many=True)

        message = "POST to /todos with 'name', 'description', 'due_date', 'status'(todo/in_progress/done), 'priority'(yes/no), 'category'(WORK/PERSONAL/SHOPPING/OTHER)."
        return Response({'data': serializer.data,'message': message})


    if request.method == 'POST':
        # Check if the request contains the required fields
        if not all(key in request.data for key in ['name', 'description', 'due_date', 'status', 'priority', 'category']):
            message = "POST to /todos with 'name', 'description', 'due_date', 'status'(todo/in_progress/done), 'priority'(yes/no), 'category'(WORK/PERSONAL/SHOPPING/OTHER)."
            return Response({'message': message}, status=status.HTTP_400_BAD_REQUEST)

        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def TodoDetails(request,pk):
    try: 
        todo = Todo.objects.get(pk=pk)
    except Todo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 