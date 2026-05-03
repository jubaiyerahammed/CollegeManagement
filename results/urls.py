from django.urls import path
from . import views



urlpatterns = [
    path('ad/', views.add_marks),
    path('um/', views.update_marks),
    path('sr/', views.student_result),
    path('cr/', views.class_result)
    
]   