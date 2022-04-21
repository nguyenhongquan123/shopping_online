from django.db import models
from django.conf import settings
from decimal import Decimal
from shop.models import Product
# Create your models here.
class Cart(object):
    
    def __init__(self,request):
        self.session=request.session
        cart=self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart=self.session[settings.CART_SESSION_ID]={}
        self.cart=cart
    
    def add(self,product,discount_percent=0,quantity=1,update=False):
        
        product_id=product.Product_id
        price=(product.price)*(100-discount_percent)/100
        if product_id  not in self.cart:
            
            self.cart[str(product_id)]={'quantity':quantity,'price':str(price)}
        else:
            if not update:
                self.cart[str(product_id)]['quantity']+=quantity
            else:
                
                self.cart[str(product_id)]['quantity']=quantity
                
        self.save()
    
    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
    
    def remove(self,product_id):
        del self.cart[str(product_id)]
        
    
    def get_total_price(self):
        total_price=0
        for product_infor in self.cart.values():
            total_price+=(product_infor['quantity']*Decimal(product_infor['price']))
        return total_price
    
    def __iter__(self):
        product_ids=self.cart.keys()
        products=Product.objects.filter(Product_id__in=product_ids)
        for product in products:
            self.cart[str(product.Product_id)]['product']=product
            
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
    
    def __len__(self):
        return len(self.cart.keys())
    
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        
                 
        