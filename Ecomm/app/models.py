from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Booking(models.Model):
    person = [
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    phone_no = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    person_count = models.IntegerField(choices=person)
    date = models.DateField()
    