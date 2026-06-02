from django.urls import path
from . import views



urlpatterns = [
    path('cl/', views.course_list),
    path('cd/', views.course_detail),
    path('cc/', views.course_create),
    path('at/', views.assign_teacher),
    path('es/', views.enroll_student),
   
    path('form/', views.show_form, name='sform'),
    path('successfully/', views.success, name='successfully')
]    