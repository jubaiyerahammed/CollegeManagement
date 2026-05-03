from django.shortcuts import render

# Create your views here.
def add_marks(request):
    return render(request,'results/add_marks.html')
def update_marks(request):
    return render(request,'results/update_marks.html')
def student_result(request):
    return render(request,'results/student_result.html')
def class_result(request):
    return render(request,'results/class_result.html')