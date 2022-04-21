from django.shortcuts import render,redirect
from django.views.generic.edit import FormView
from cart.forms import CartAddProduct
from django.http import HttpResponse
from django.views import View
from coupons.models import Coupon
from django.core.exceptions import ValidationError
from cart.views import addProductCart
import pickle
# Create your views here.
from shop.models import Product
class add_product_cart_site(FormView):
    template_name='products/detail.html'
    form_class = CartAddProduct
    def get(self,request,slug):
        try:
            product=Product.objects.get(slug=slug)
        except:
            product=None
       
        return self.render_to_response(self.get_context_data(product=product))
    
    def form_valid(self, form):
        cd=form.cleaned_data
        try:
            coupon=Coupon.objects.get(code=cd['code'])
        except:
            coupon=None
        return addProductCart(self.request,1,1)
        


    


    