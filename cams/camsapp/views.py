from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    my_dict={'insert_me':"Hello i am from views.py "}
    return render(request, "index.html",context=my_dict)

def home(request):
    return render(request, "home.html",{})

def about(request):

    return render(request, "about.html",{})

def contact(request):
    return render(request, "contact.html",{})

def login(request):
    return render(request, "users/login.html",{})
