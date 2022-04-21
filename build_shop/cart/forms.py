from wsgiref.validate import validator
from django import forms
from django.core.exceptions import ValidationError
PRODUCT_QUANTITY_CHOICES=[ (i,str(i) )for i in range(1,21)]
def check_quantity(value):
    if int(value)<1:
        raise ValidationError('<0')
    
class CartAddProduct(forms.Form):
    
    quantity = forms.TypedChoiceField(
        choices=PRODUCT_QUANTITY_CHOICES,
        coerce=int,validators=[check_quantity])
    update = forms.BooleanField(required=False,
                                initial=False,
                                )
    code=forms.CharField(required=False)

class PostCommentForm(forms.Form):
    body=forms.CharField(widget=forms.TextInput,required=True)
    # product=forms.HiddenInput()
    # def __init__(self,request,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
        # self.fields['product'].widget.attrs.update({'class':'form-control',})
        