from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def student_list(request):
    return render (request,'students/student_list.html')
def student_detail(request):
    return render (request,'students/student_detail.html')
def student_create(request):
    return render (request,'students/student_create.html')
def student_update(request):
    return render (request,'students/student_update.html')
def student_delete(request):
    return render (request,'students/student_delete.html')


