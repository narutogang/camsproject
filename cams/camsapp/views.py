from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html",{})

def home(request):
    return render(request, "home.html",{})

def about(request):
    from cmspages.namer import bob
    return render(request, "about.html",{"my_stuff":bob})

def contact(request):
    return render(request, "contact.html",{})

def login(request):
    return render(request, "login.html",{})