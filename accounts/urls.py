from django.urls import path
from . import views



urlpatterns = [
    path('li/', views.login_view),
    path('lo/', views.logout_view),
    path('rs/', views.register_student),
    path('rt/', views.register_teacher),
    
]    