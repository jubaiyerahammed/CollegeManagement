
from django.urls import path
from . import views



urlpatterns = [
    path('sl/', views.student_list),
    path('sd/', views.student_detail),
    path('sc/', views.student_create),
    path('su/', views.student_update),
    path('sde/', views.student_delete),
    
]  