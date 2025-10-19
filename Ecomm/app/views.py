from django.shortcuts import render,redirect
from .models import Booking

# Create your views here.
def home (request):
    return render(request,"app/index.html",{})

def landing (request):
    return render (request , "app/landing.html")   

def menu(request):
    context = {
        "lat": 18.9228,
        "lon": 72.8317,
        "api_key": "c22c22aa0aed46e5bf788d2004d335b3",
    }
    if request.method == 'POST':
        return redirect('cart')
    return render(request, "app/menu.html", context)

def cart (request):
    return render (request, "app/cart.html")

def BookingTable(request):
    if request.method == 'POST':
        user = request.user
        Booking.objects.create(
            user=user,
            name=request.POST.get('name'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            person_count=request.POST.get('person_count'),
            date=request.POST.get('date'),
        )
        return redirect('menu')
    return render(request, "app/Bookingtable.html")

    
    