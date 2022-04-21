from django import forms
from .models import Order
from shop.models import Product
from User.models import DeliveryInfor

# PRODUCT_LIST=(
    
# )

class OrderCreateForm(forms.ModelForm):
    
    class Meta:
        model = Order
        fields=['id','name','paid','slug','delivery_infor']
        
    def __init__(self,request,*arg,**kwargs):
        super().__init__(*arg,**kwargs)
        
        for field in self.fields:
            if field not in ['delivery_infor','products','paid']:
                self.fields[field].widget.attrs.update({'class':'form-control'})
            
            if field =="delivery_infor":
                self.fields[field]=forms.ModelChoiceField(queryset=request.user.customer.delivery_infor.all())
            
            
    
                
        
    
        
        
        
    
        
