from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path('analytics/', views.dashboard_analytics, name='dashboard_analytics')

]
