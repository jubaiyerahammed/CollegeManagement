
from django.urls import path
from . import views



urlpatterns = [
    path('sl/', views.student_list),
    path('sd/', views.student_detail),
    path('sc/', views.student_create),
    path('su/', views.student_update),
    path('sde/', views.student_delete),
    path('si/', views.student_info, name='st_info'),
    path('form/', views.show_form, name='sform'),
    path('successfully/', views.success, name='successfully'),
    path("add/", views.student_add, name="student_add"),

    
]  