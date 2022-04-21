from django.db import models
from django.urls import reverse
# Create your models here.

   
class Category(models.Model):
    Cate_id=models.CharField(max_length=12,primary_key=True)
    Name=models.CharField(max_length=20)
    Slug=models.SlugField(max_length=200,unique=True)
    
    class Meta:
        ordering = ('Name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.Name

class Product(models.Model):
    Product_id=models.CharField(max_length=12,primary_key=True)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True,default='')
    image=models.ImageField(upload_to="products/%Y/%m/%d")
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('cart:add_product_cart',args=[self.slug])

    

    
    
    