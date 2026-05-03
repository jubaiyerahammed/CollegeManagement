from django.urls import path
from . import views



urlpatterns = [
   path('ta/', views.take_attendance),
   
    
]    