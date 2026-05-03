from django.shortcuts import render

# Create your views here.
def teacher_list(request):
    return render(request,'teachers/teacher_list.html')
def teacher_detail(request):
    return render(request,'teachers/teacher_detail.html')
def teacher_create(request):
    return render(request,'teachers/teacher_create.html')
def teacher_update(request):
    return render(request,'teachers/teacher_update.html')
def teacher_delate(request):
    return render(request,'teachers/teacher_delate.html')

