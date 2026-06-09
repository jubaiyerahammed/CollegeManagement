from django.shortcuts import render
from . forms import StudentRegistration
from . models import StudentsInfo
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
            cleaned = frm.cleaned_data
            fname= cleaned['first_name']
            lname=cleaned['last_name']
            eml=cleaned['email']
            btc=cleaned['batch']
            pas=cleaned['password']
            rpas=cleaned['re_password']
            txt=cleaned['textarea']
            pay=cleaned['payments']
            Datapsql= StudentsInfo( first_name=fname, last_name=lname, email=eml, batch=btc, password=pas, re_password=rpas, textarea=txt, payments=pay)
            Datapsql.save()
            return HttpResponseRedirect('/cr/successfully')
    else:
        frm= StudentRegistration( label_suffix='###')
        frm.order_fields(field_order= ['email','first name', 'last name', 'batch'])
        print('Execute GET')

    return render(request, 'courses/forms.html', {'form':frm})

def success(request):
    return render(request,'courses/submit.html')

def course_add(request):
    return render(request, "courses/course_add.html")
