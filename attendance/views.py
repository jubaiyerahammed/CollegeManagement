from django.shortcuts import render

# Create your views here.
def take_attendance(request):
    return render(request,'attendance/take_attendance.html')
def attendance_report_teacher(request):
    return render(request,'attendance/attendance_report_teacher.html')
def attendance_report_student(request):
    return render(request,'attendance/attendance_report_student.html')