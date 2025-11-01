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
    prd_price = models.IntegerField()
    prd_image = models.ImageField(upload_to='producting/', null=True, blank=True)
    prd_description = models.TextField()
    prd_type = models.CharField(max_length=20, choices=types)

    def __str__(self):
        return self.prd_name


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderItem)

    def __str__(self):
        return f"{self.user.username}'s Cart"
