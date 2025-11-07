from django.shortcuts import render,redirect
from .models import Booking,OrderItem,Cart
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from .forms import CreateUser
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

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
    user = request.user 
    items = Cart.objects.filter(user=user)
    
    if request.method=='POST':
        form_type = request.POST.get('btn-cart')
        id_to_delete = form_type
        Cart.objects.get(id = id_to_delete).delete()
    return render (request, "app/cart.html",{'item':items})

def send_inc_data(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        obj = Cart.objects.get(id = data['id'])
        obj.prd_quantity = obj.prd_quantity + 1 
        obj.save()
        return JsonResponse({'value': obj.prd_quantity})


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

def send_cart_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data['prd_name']
            desc = data['desc']
            img_src = data['img_src']
            price = data['price']
            user = request.user
            Cart.objects.create(user = user,cart_prd_name = name,cart_prd_price= price,cart_prd_description= desc,cart_prd_image=img_src)
            
            response = {
                'message':'item added successfully'
            }
            return JsonResponse(response)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Only POST method allowed"}, status=405)
        
def entry(request):
    signup_form = CreateUser()
    login_form = AuthenticationForm()

    if request.method == 'POST':
        form_name = request.POST.get('form_name')

        # ---- SIGNUP FORM ----
        if form_name == 'signup_form':
            signup_form = CreateUser(request.POST)
            if signup_form.is_valid():
                user = signup_form.save()
                login(request, user)
                messages.success(request, f"Welcome, {user.username}!")
                return redirect('menu')
            else:
                messages.error(request, "Invalid signup details.")

        # ---- LOGIN FORM ----
        elif form_name == 'login_form':
            login_form = AuthenticationForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                messages.success(request, f"Welcome back, {user.username}!")
                return redirect('menu')
            else:
                messages.error(request, "Invalid login credentials.")

    return render(
        request,
        "app/login_signup.html",
        {
            'signup_form': signup_form,
            'login_form': login_form
        }
    )