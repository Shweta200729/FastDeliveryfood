from django.contrib import admin
from .models import Booking,OrderItem,Cart

# Register your models here.
admin.site.register(Booking)
admin.site.register(OrderItem)
admin.site.register(Cart)