from django.urls import path
from . import views



urlpatterns = [
    path('li/', views.login_view, name='login_view'),
    path('lo/', views.logout_view, name='logout'),
    path('rs/', views.register_student, name='register_student'),
    path('rt/', views.register_teacher, name='register_teacher'),
    path('login/', views.login, name='login'),
    path('menu/',views.menu, name="menu"),
    path('withdraw/',views.withdraw, name="withdraw"),
    path('deposit/', views.deposit, name="deposit"),
    path('balance/',views.balance, name="balance"),

]    