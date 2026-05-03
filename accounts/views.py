from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login_view(request):
    return render(request,'accounts/login_view.html')
def logout_view(request):
    return render (request,'accounts/logout_view.html')
def register_student(request):
    return render (request,'accounts/register_student.html')
def register_teacher(request):
    return render (request,'accounts/register_teacher.html')
