from django.shortcuts import render
from . forms import StudentRegistration
from django.http import HttpResponseRedirect
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

def show_form(request):
    if request.method=='POST':
        frm=StudentRegistration(request.POST)
        if frm.is_valid():
            print(frm)
            print('Execute POST')
            print(frm.cleaned_data)
            return HttpResponseRedirect('/cr/successfully')
    else:
        frm= StudentRegistration( label_suffix='###')
        frm.order_fields(field_order= ['email','first name', 'last name', 'batch'])
        print('Execute GET')

    return render(request, 'courses/forms.html', {'form':frm})

def success(request):
    return render(request,'courses/submit.html')