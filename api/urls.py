from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter() 
router.register('employees', views.EmployeeViewset, basename='employee')


urlpatterns = [
    path('students/', views.studentsview),
    path('students/<int:pk>/', views.studentdetailview),
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/', views.Employeedetailview.as_view()),
    
    path('', include(router.urls)),
    
    path('blogs/', views.BlogsView.as_view()),
    path('comment/', views.CommentsView.as_view())
]
