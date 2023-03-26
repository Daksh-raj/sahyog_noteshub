from django.shortcuts import render, HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

# Create your views here.


def index(request):
    return render(request,"home.html")


def btech(request):
    return render(request, "btech.html")

def mtech(request):
    return render(request,"mtech.html")

def phd(request):
    return render(request,"phd.html")


def home(request):
    return render(request,"home.html")

def about(request):
    return render(request,"about.html")

def nn(request):
    return HttpResponse("404 Not found")
