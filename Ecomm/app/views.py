from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request,"app/index.html",{})

def landing (request):
    return render (request , "app/landing.html")   

def menu (request):
    return render (request, "app/menu.html")