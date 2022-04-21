from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render,get_object_or_404
from .models import Cart
from .forms import CartAddProduct , PostCommentForm
from shop.models import Product
from django.views.generic import TemplateView 
from django.views.generic.edit import FormView
from django.views import View
from coupons.models import Coupon
from django.core.exceptions import ValidationError
from shop.recomender import Recommender
from actions.models import *
from django.contrib.contenttypes.models import ContentType
from django.views.decorators.http import require_POST

# Create your views here.

class DetailCart(TemplateView):
    template_name='cart/detail_cart.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['cart']=Cart(self.request)
        return context


class AddProductCart(TemplateView):
    template_name='cart/add_product_cart.html'
    cart_add_form = CartAddProduct()
    post_comment_form=PostCommentForm()
    context={}
    def get(self,request,slug=None):
        try:
            product=Product.objects.get(slug=slug)
        except:
            product=None
        #call get_context_data
        context_data=self.get_context_data()
        print("context:",context_data)
        
        #form 
        context_data['cart_add_form']=self.cart_add_form    
        context_data['post_comment_form']=self.post_comment_form
        
        #recommender system
        re=Recommender()
        flag_ids=re.suggest_products_for(product.Product_id)
        context_data['product']=product
        
        if flag_ids!=None:
            recommended_products=Product.objects.filter(Product_id__in=flag_ids)
            context_data['recommended_products']=recommended_products
            
                  
        
        #comments
        comment_type=ContentType.objects.get(app_label='actions',model='Comment') 
        comments=Action.objects.filter(product=product,content_type=comment_type) 
        context_data['comments']=comments   
        
        #update context
        self.context.update(context_data)              
        return self.render_to_response(self.context)
    
    
    def post(self,request,slug):
        
        if request.POST.get('form-type')=='card-add-form':
            form=CartAddProduct(request.POST)
            if form.is_valid():    
                cd=form.cleaned_data
                try:
                    coupon=Coupon.objects.get(code=cd['code'])
                except:
                    coupon=None
                return addProductCart(self.request,self.context['product'],coupon,cd)
        return HttpResponse("fail!") 
        
@require_POST
def post_Comment(request):
    if request.POST.get('form-type')=='post-comment-form' and request.is_ajax():
        from django.utils.timezone import now
        form=PostCommentForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            
            #create Comment object
            import random
            while True:
                id_comment_instance=str(random.randint(0,10^20))
                
                if id_comment_instance not in Comment.objects.values_list('id',flat=True):
                    break
            Comment.objects.create(
                    id=id_comment_instance,
                    body=cd['body']
            )
            #create Action
            
            action_instance=Action.objects.create(
                user=request.user,
                product=Product.objects.get(Product_id=request.POST.get('product_id')),
                content_type=ContentType.objects.get(
                    app_label='actions',
                    model='Comment'),
                object_id=id_comment_instance
            )
            print("::::::::::",action_instance.create_at)
            return JsonResponse({'valid':True,'time':action_instance.create_at})
        else:
            return JsonResponse({'valid':False})
            


        

    
def addProductCart(request,product,coupon,cd):
    cart=Cart(request)
    if coupon is not None:
        discount=coupon.discount
    else:
        discount=0
    cart.add(product,discount,cd['quantity'],cd['update'])
    cart.save()
    return redirect('cart:detail_cart')

def deleteProductCart(request,product_id):
    cart=Cart(request)
    cart.remove(product_id)
    cart.save()
    return JsonResponse({'valid':True,'total_price':cart.get_total_price()})

# def checkoutCart(request):

#     return HttpResponse("check out") 

class test(TemplateView):
    template_name='cc.html'
    def get(self,request,quan):
        try:
            print("::::::::::::::::",quan)
            
        except:
            pass
        return super().get(request)
    def post(self,request):
        return HttpResponse("oke")