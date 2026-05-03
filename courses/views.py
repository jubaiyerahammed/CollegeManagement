from django.shortcuts import render

# Create your views here.
def course_list(request):
    return render(request,'courses/course_list.html')
def course_detail(request):
    return render(request,'courses/course_detail.html')
def course_create(request):
    return render(request,'courses/course_create.html')
def assign_teacher(request):
    return render(request,'courses/assign_teacher.html')
def enroll_student(request):
    return render(request,'courses/enroll_student.html')