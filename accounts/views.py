from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render, redirect
from .models import Account
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import RegistrationForm

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts:login")
    else:
        form = RegistrationForm()
    return render(request, "accounts/register.html", {"form": form})
# def login(request):
#     if request.method == "POST":
#         pin = request.POST.get("pin")
#         try:
#             account = Account.objects.get(pin=pin)
#             request.session["account_id"] = account.id
#             return redirect("menu")
#         except:
#             return render(request, "accounts/login.html", {"error": "Wrong PIN"})
#     return render(request, "accounts/login.html")
def menu(request):
    return render(request, "accounts/menu.html")
def withdraw(request):
    account_id = request.session.get("account_id")

    # যদি session এ account_id না থাকে → login এ পাঠাও
    if not account_id:
        return redirect("login")

    account = Account.objects.get(id=account_id)

    if request.method == "POST":
        amount = int(request.POST.get("amount"))

        if amount <= 0:
            msg = "Amount must be positive"
        elif amount > 50000:
            msg = "Maximum withdrawal limit is 50000"
        elif amount > account.balance:
            msg = "Insufficient balance"
        else:
            account.balance -= amount
            account.save()
            msg = f"Withdrawal successful! New balance: {account.balance}"

        return render(request, "accounts/withdraw.html", {"msg": msg})

    return render(request, "accounts/withdraw.html")

def deposit(request):
    account = Account.objects.get(id=request.session["account_id"])

    if request.method == "POST":
        amount = int(request.POST.get("amount"))

        if amount < 1000:
            msg = "Minimum deposit is 1000"
        elif amount > 50000:
            msg = "Maximum deposit limit is 50000"
        else:
            account.balance += amount
            account.save()
            msg = f"Deposit successful! New balance: {account.balance}"

        return render(request, "accounts/deposit.html", {"msg": msg})

    return render(request, "accounts/deposit.html")

def balance(request):
    account = Account.objects.get(id=request.session["account_id"])
    return render(request, "accounts/balance.html", {"balance": account.balance})



def login_view(request):
    return render (request,'accounts/login_view.html')    
def logout_view(request):
    return render (request,'accounts/logout_view.html')
def register_student(request):
    return render (request,'accounts/register_student.html')
def register_teacher(request):
    return render (request,'accounts/register_teacher.html')


def profile(request):
    return render(request, "accounts/profile.html")

def my_account(request):
    return render(request, "accounts/my_account.html")

