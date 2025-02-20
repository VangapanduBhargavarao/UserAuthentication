from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES=[
            ('patient','patient'),
            ('doctor','doctor'),
    ]
    FirstName=models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)
    role=models.CharField(max_length=10,choices=ROLE_CHOICES,default='patient')
    profile_picture=models.ImageField(upload_to='profile_pics/',blank=True,null=True)
    address_line1=models.CharField(max_length=255)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.CharField(max_length=100)

    def __str__(self):
        return self.username