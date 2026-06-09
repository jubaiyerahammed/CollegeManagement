from django.shortcuts import render
from django.http import HttpResponse
from . models import Student
from . forms import StudentRegistration
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import StudentForm
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
            return HttpResponseRedirect('/st/successfully/')

    else:

        frm= StudentRegistration(label_suffix='##', initial={'email':'jubaiy@gmail.com'})
        frm.order_fields(field_order=['email','first_name','last_name', 'batch'])
        print('Execute.GET')
    return render (request, 'students/forms.html', {'forms':frm})
def success(request):
    return render(request, 'students/submit.html')

def student_add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student_add")  # redirect to same page or student list
    else:
        form = StudentForm()

    return render(request, "students/student_add.html", {"form": form})

