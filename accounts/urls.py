from django.urls import path
from . import views



urlpatterns = [
    path('li/', views.login_view, name='login'),
    path('lo/', views.logout_view, name='logout'),
    path('rs/', views.register_student, name='register_student'),
    path('rt/', views.register_teacher, name='register_teacher'),
    
]    