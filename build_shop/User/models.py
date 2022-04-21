
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=200)
    is_owner=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=False)
        
class Customer(models.Model):
    user=models.OneToOneField(User,unique=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return "Customer : {}".format(self.user.name)
    
class Owner(models.Model):
    user=models.OneToOneField(User,unique=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return "Owner : {}".format(self.user.name)
    
    
class DeliveryInfor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number=models.CharField(max_length=255)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    customer=models.ForeignKey(Customer,related_name='delivery_infor',on_delete=models.CASCADE)
    
    def __str__(self):
        return "{}-{}".format(self.last_name,self.id)