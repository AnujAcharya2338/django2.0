from django.shortcuts import render
from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer, EmployeeSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404
from rest_framework import mixins,generics
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
    
@api_view(['GET','PUT','DELETE'])
def studentdetailview(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
           serializers = StudentSerializer(student, data = request.data)
           if serializers.is_valid():
               serializers.save();
               return Response(serializers.data, status=status.HTTP_200_OK)
           else:
               return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 
           
    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# class Employees(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializers(employees, many = True)
        
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def post(self, request):
#         serializers = EmployeeSerializers(data = request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 
            
# class Employeedetailview(APIView):
#     def get_object(self, pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404
            
#     def get(self, request, pk):
#         employee = self.get_object(pk)
#         serialier = EmployeeSerializers(employee)
#         return Response(serialier.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializers (employee, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

           
      
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):  
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    
    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)

        
class Employeedetailview(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    
    def get(self, request, pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self,request,pk):
        return self.destroy(request, pk)
        


        
        



        
        
        