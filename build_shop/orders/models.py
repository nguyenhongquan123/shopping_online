from django.db import models
from User.models import Customer,DeliveryInfor
from shop.models import Product
# Create your models here.

class Order(models.Model):
    id=models.CharField(primary_key=True, max_length=12)
    name=models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    slug=models.SlugField(unique=True)
    products=models.ManyToManyField(Product,related_name='products',through='OrderItem')
    delivery_infor=models.ForeignKey(DeliveryInfor,on_delete=models.CASCADE)
    
    
    class Meta:
        ordering = ('-created',)
        
    def __str__(self):
        return 'Order-{}-{}'.format(self.name,self.id)
    
    def get_total_cost(self):
        items=OrderItem.objects.filter(order=self)
        return sum([item.price*item.quantity for item in items])
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_items',on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    

    