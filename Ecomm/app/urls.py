from django.urls import path
from . import views
urlpatterns = [
    path("" , views.landing, name="landing"),
    path("menu/" , views.menu, name="menu"),
    path('items/',views.items, name= 'items'),
    path("cart/" , views.cart, name="cart"),
    path("BookingTable/" , views.BookingTable, name="BookingTable"),

]
