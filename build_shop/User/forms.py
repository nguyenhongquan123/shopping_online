from django import forms
from .models import DeliveryInfor
# Create your views here.
class AddDeliveryUserForm(forms.ModelForm):
    class Meta:
        model = DeliveryInfor
        fields = ['first_name', 'last_name', 'email','phone_number', 'address', 'postal_code', 'city']
        # widgets={
        #     'customer':forms.HiddenInput(),
        # }

    def __init__(self,*arg,**args):
        super().__init__(*arg,**args)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
        print(self.fields)
        