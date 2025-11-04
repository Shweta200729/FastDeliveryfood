from django.urls import path
from . import views
urlpatterns = [
    path("" , views.landing, name="landing"),
    path("menu/" , views.menu, name="menu"),
    path('items/',views.items, name= 'items'),
    path("cart/" , views.cart, name="cart"),
    path("BookingTable/" , views.BookingTable, name="BookingTable"),
    path("RenderItem/" , views.RenderItem, name='render'),
    path("send_cart_data/",views.send_cart_data , name = 'send_cart_data'),
    path("send_inc_data/",views.send_inc_data, name = 'send_inc_data')
]
