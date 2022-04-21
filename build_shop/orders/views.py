from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse,JsonResponse
from User.models import *
from User.models import Customer
from .models import OrderItem
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from cart.models import Cart
from .forms import OrderCreateForm
from .models import Order,OrderItem
from django.views import View
from django.utils import timezone
from django.db.models import Count ,F,Sum
from shop.recomender import *
from .tasks import order_created
class Order_Detail(TemplateView):
    template_name='orders/orders_detail.html'
    
    def get(self, request, slug=None):
        user=self.request.user
        orders=Order.objects.filter(delivery_infor__customer__user=user)
        if slug is not None:
            order=Order.objects.get(slug=slug)
        else:
            order=Order.objects.first()
        order_items=OrderItem.objects.filter(order=order).annotate(total_price=F('price')*F('quantity'))
        total_cost_order=order_items.aggregate(Sum('total_price'))['total_price__sum']
        # print(total_cost_order['total_price__sum'])
        return super().get(request,orders=orders,order_items=order_items,total_cost_order=total_cost_order)
        
    
class CreateOrder(View):
    def get(self ,request):
        form=OrderCreateForm(request=request)
        return render(request,'orders/create_order.html',{'form':form})
    
    def post(self,request):
            cart = Cart(request)
            form=OrderCreateForm(request,request.POST)
            re=Recommender()
            list_product=[]
            
            if form.is_valid():
                try:
                    instance=Order.objects.get(id=request.POST['id'])
                except:
                    instance=None
                if instance is  None:
                    # print(form.cleaned_data)
                    order=form.save()
                    for item in cart:
                        OrderItem.objects.create(order=order,
                                                product=item['product'],
                                                price=item['price'],
                                                quantity=item['quantity'])
                        list_product.append(item['product'])
                    # get infor of product to recommend next product
                    re.products_bought(list_product) 
                    
                    cart.clear()
            
                    # task=order_created.delay('1')
                    # print(f"id={task.id}, state={task.state}, status={task.status}") 
                    return redirect('orders:order_detail_all')
            return HttpResponse("fail!")
    

def validateId(request):
        if request.is_ajax:
            try:
                instance=Order.objects.get(id=request.POST['id'])
            except:
                instance=None
        if instance is None:
            check=True
        else:
            check=False
        return JsonResponse({'valid':check})
# def checkDuplicateId(request):
    
        
        
        
from time import sleep

def index(request):
    sleep(5)
    print("hih")
    return render(request,'cc.html')