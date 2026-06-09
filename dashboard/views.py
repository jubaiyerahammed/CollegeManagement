from django.shortcuts import render
from students.models import Student
from teachers.models import Teacher
from courses.models import Course
from dashboard.models import Activity, Event


def dashboard(request):
    """Main Dashboard Overview"""

    student_count = Student.objects.count()
    teacher_count = Teacher.objects.count()
    course_count = Course.objects.count()

    recent_activities = Activity.objects.order_by("-created_at")[:5]
    upcoming_events = Event.objects.order_by("date")[:5]

    context = {
        "student_count": student_count,
        "teacher_count": teacher_count,
        "course_count": course_count,
        "revenue": 125000,  # Static demo value

        "recent_activities": recent_activities if recent_activities else ["No recent activity"],
        "upcoming_events": upcoming_events if upcoming_events else ["No upcoming events"],
    }

    return render(request, "dashboard/dashboard.html", context)



def dashboard_analytics(request):
    """Analytics Dashboard Page"""

    context = {
        "student_count": Student.objects.count(),
        "teacher_count": Teacher.objects.count(),
        "course_count": Course.objects.count(),
    }

    return render(request, "dashboard/analytics.html", context)
