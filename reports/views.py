from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def generate_report(request):
    return render(request, "reports/generate_report.html")
