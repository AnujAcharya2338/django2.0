from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST'])
def studentsview(request):
    if request.method == "GET":
        student = Student.objects.all()
        serizlizers = StudentSerializer(student, many=True)
        return Response(serizlizers.data, status=status.HTTP_200_OK)
    
    elif request.method == "POST":
        serizlizers = StudentSerializer(data = request.data)
        if serizlizers.is_valid():
            serizlizers.save()
            return Response(serizlizers.data, status=status.HTTP_201_CREATED)
        return Response(serizlizers.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def studentdetailview(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)