from django.http import JsonResponse
from django.shortcuts import redirect, render,HttpResponse
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login,logout
from .forms import *
from pprint import  pprint
from django.db.models import Q
from shop.models import Category,Product
import json
from django.contrib.auth.decorators import login_required
# Create your views here.
class Home(LoginRequiredMixin,TemplateView):
    template_name="home/index.html"
    login_url='home:login-register'
    
    def get(self, request):
        request.session['color']='reds'
        print(request.session['color'])
        categories=Category.objects.all()
        products=Product.objects.all()
        return super().get(request,products=products,categories=categories)    
    
    def post(self,request):
        cate_filter=[];price_filter=[]
        for i in request.POST:
            try:
                index=int(i.index('-'))
                flag=i[0:index]
                name_filter=i[index+1:]
                if flag=='cate':
                    cate_filter.append(name_filter)
                if flag=='price':
                    price_filter.append( request.POST.get(i))
            except:
                pass

        products=Product.objects.filter(Q(Category__Name__in=cate_filter))
        products=products.filter(Q(price__gte=float(price_filter[0])),Q(price__lte=float(price_filter[1])) )
        categories = Category.objects.all()
        return render(request,
                    'home/index.html',{
                    'categories': categories,
                    'products': products})
        
        
class SiteLoginRegister(TemplateView):    
    template_name='home/login-register.html'
    login_form=LoginForm()
    register_form=RegisterForm()
    
    def get(self,request):
        return super().get(request)
    
    def post(self,request):
        
        # login form..
        if request.POST.get('form-type')=='login_form' and request.is_ajax() :
            login_form=LoginForm(request.POST)
            valid=False;flag=False;is_admin=False
            tmp={}
            if login_form.is_valid():
                cd=login_form.cleaned_data
                message_error=[]
                user = authenticate(username=cd['username']
                                    ,password=cd['password'])
                is_admin=cd['is_admin']
                if user is not None:
                    login(request,user=user)
                    valid=True 
                    request.session.set_expiry(0)
                else:
                    flag=True
            error_dict=dict(login_form.errors.items())
            if flag==True:
                error_dict['mess_account']=["Account is not correct!"]
            error_dict=json.dumps(error_dict)
            return JsonResponse({'valid':valid,
                                 'is_admin':is_admin,
                                 'error_dict':error_dict}
                                )
        return HttpResponse("Fail")    
               
                
                #      return self.render_to_response(
                #          self.get_context_data(message="loi nha!")
                #         )   
                       
        
        # register form..    
        if request.POST.get('form-type')=='register_form':
            register_form=RegisterForm(request.POST)
            if register_form.is_valid():
                return HttpResponse("C")
            else:
                return self.render_to_response(self.get_context_data(register_form=register_form))
            
    def get_context_data(self,login_form=None,register_form=None,**kwargs):
        context=super().get_context_data() 
        for key,value in kwargs.items():
            context[key]=value
        if login_form is  None:
            login_form=self.login_form
        if register_form is  None:
            register_form=self.register_form
            
        context['login_form']=login_form    
        context['register_form']=register_form
        return context
                
       


def logout_function(request):
    logout(request)
    return redirect('home:login-register')


class regis(FormView):
    form_class=LoginForm
    template_name='cc.html'
    
    def form_valid(self, form):
        cd=form.cleaned_data
        message_error=[]
        user = authenticate(username=cd['username']
                            ,password=cd['password'])
        if user is not None:
            pass
            login(self.request,user=user)
            return redirect("management:dashboard")
        
    def form_invalid(self, form):
        
        return super().form_invalid(form)
    

def check_odecoratorwner(user):
    return user.is_owner


# @user_passes_test(check_owner,login_url="home:cc")


# @only_admin(context="acess denied")
# @user_passes_test(check_owner,login_url="home:cc")
# def dashboard(request):   
#     return HttpResponse("dashboard")

# from django.contrib.auth.mixins import UserPassesTestMixin

# class vdashboard(UserPassesTestMixin,TemplateView):
#     login_url="home:cc"
    
#     def test_func(self):
#         return True
    
#     def get(self,request):
#         return HttpResponse("dashboard!")    


    
    
        
        
        
        
    
        