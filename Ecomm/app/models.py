from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    PERSON_CHOICES = [
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    phone_no = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    person_count = models.IntegerField(choices=PERSON_CHOICES)
    date = models.DateField()

    def __str__(self):
        return self.name

class OrderItem(models.Model):
    types = [
        ('Starter', 'Starter'),
        ('Main_course', 'Main_course'),
        ('Beverages', 'Beverages'),
        ('Dessert', 'Dessert'),
    ]

    prd_name = models.CharField(max_length=50, unique=True)
    prd_price = models.IntegerField(default=0)
    prd_image = models.ImageField(upload_to='producting/', null=True, blank=True)
    prd_description = models.TextField()
    prd_type = models.CharField(max_length=20, choices=types)
    prd_quantity = models.PositiveIntegerField(default = 1)
    def __str__(self):
        return self.prd_name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart_prd_name = models.CharField(max_length=50)
    cart_prd_price = models.IntegerField(default=0)
    cart_prd_description = models.TextField(blank=True)
    cart_prd_image = models.URLField(max_length=300, blank=True, null=True)

    def __str__(self):
        return f"{self.cart_prd_name} - ₹{self.cart_prd_price}"

class UserTotal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.PositiveIntegerField(default=0)