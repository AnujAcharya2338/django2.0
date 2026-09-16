from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentsview),
    path('students/<int:pk>/', views.studentdetailview),
]
