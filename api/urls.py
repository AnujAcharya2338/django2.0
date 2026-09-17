from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentsview),
    path('students/<int:pk>/', views.studentdetailview),
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.Employeedetailview.as_view()),
]
