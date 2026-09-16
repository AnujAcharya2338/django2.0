from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def studentsview(request):
    students = {
        'id':1,
        'name':'Anuj Acharya',
        'Age':21,
    }
    
    return JsonResponse(students)