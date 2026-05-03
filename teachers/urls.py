from django.urls import path
from . import views



urlpatterns = [
    path('tl/', views.teacher_list),
    path('td/', views.teacher_detail),
    path('tc/', views.teacher_create),
    path('tu/', views.teacher_update),
    path('tde/', views.teacher_delate)

]    