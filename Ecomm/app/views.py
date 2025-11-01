from django.shortcuts import render,redirect
from .models import Booking,OrderItem
from django.http import JsonResponse

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
        return redirect('items')
    return render(request, "app/menu.html", context)

def items(request):
    if request.method == 'POST':
        form_type = request.POST.get('btn_type')
        if form_type == 'cart':
            return redirect('cart')
    return render(request,'app/items.html')

def cart (request): 
    return render (request, "app/cart.html")

def BookingTable(request):
    if request.method == 'POST':
        user = request.user
        Booking.objects.create(
        user=user,
        name=request.POST.get('name'),
        phone_no=request.POST.get('phone'),
        email=request.POST.get('email'),
        person_count=request.POST.get('person_count'),
        date=request.POST.get('date'),
)

        return redirect('menu')
    return render(request, "app/Bookingtable.html")


def RenderItem(request):
    Starter_items = OrderItem.objects.filter(prd_type='Starter')
    main_course = OrderItem.objects.filter(prd_type='Main_course')
    beverages = OrderItem.objects.filter(prd_type='Beverages')
    dessert = OrderItem.objects.filter(prd_type='Dessert')
    
    starter_list = []
    for item in Starter_items:
        starter_list.append({
            'name': item.prd_name,
            'desc': item.prd_description,
            'price': item.prd_price,
            'img': item.prd_image.url if item.prd_image else ''
        })

    main_course_list = []
    for item in main_course:
        main_course_list.append({
            'name': item.prd_name,
            'desc': item.prd_description,
            'price': item.prd_price,
            'img': item.prd_image.url if item.prd_image else ''
        })

    beverages_list = []
    for item in beverages:
        beverages_list.append({
            'name': item.prd_name,
            'desc': item.prd_description,
            'price': item.prd_price,
            'img': item.prd_image.url if item.prd_image else ''
        })

    dessert_list = []
    for item in dessert:
        dessert_list.append({
            'name': item.prd_name,
            'desc': item.prd_description,
            'price': item.prd_price,
            'img': item.prd_image.url if item.prd_image else ''
        })
        
    data = {    
        'Starters': starter_list,
        'Main Course': main_course_list,
        'Beverages': beverages_list,
        'Desserts': dessert_list
    }
    return JsonResponse(data)
