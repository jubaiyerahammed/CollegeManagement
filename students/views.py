from django.shortcuts import render
from django.http import HttpResponse
from . models import Student
from . forms import StudentRegistration
from django.http import HttpResponseRedirect
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

def student_info (request):
   student_details=Student.objects.all()

   return render (request,'students/std.html', {'std':student_details} ) 


def show_form(request):
    if request.method== 'POST':
        frm = StudentRegistration(request.POST)
        if frm.is_valid():
            print(frm)
            print('Execute.GET')
            print(frm.cleaned_data)
            return HttpResponseRedirect('/successfully')

    else:

        frm= StudentRegistration(label_suffix='##', initial={'email':'jubaiy@gmail.com'})
        frm.order_fields(field_order=['email','first_name','last_name', 'batch'])
        print('Execute.GET')
    return render (request, 'students/forms.html', {'forms':frm})
def success(request):
    return render(request, 'students/submit.html')
