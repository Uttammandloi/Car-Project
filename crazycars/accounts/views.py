from django.shortcuts import render ,redirect

# Create your views here.
from django.shortcuts import render


def Login(request):
    return render(request,"accounts/login.html")

def Register(request):
    return render(request,"accounts/register.html")

def Dashboard(request):
    return render(request,"accounts/dashboard.html")

def Logout(request):
    return redirect("home")
