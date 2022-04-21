from django import forms
from django.core.exceptions import ValidationError


    
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(),required=True)
    password = forms.CharField(widget=forms.PasswordInput(),required=True)
    is_admin=forms.BooleanField(required=False)
    
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({ 'class':'input'})
    def clean(self):
        super().clean()
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if len(username) >10:
            self.add_error('username','nho hon 5')
        if len(password)>5:
            self.add_error('password','nho hon 5')
            self.add_error('password','nho hon 4')
            
        return self.cleaned_data 
class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'id':1,'placeholder':'Username'}),required=True)
    password_1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password_1'}),required=True)
    password_2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password_2'}),required=True)
        
        
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({ 'class':'input'})
            
    def clean(self):
        super().clean()
        username = self.cleaned_data.get('username')
        password_1 = self.cleaned_data.get('password_1')
        password_2 = self.cleaned_data.get('password_2')
        if password_1!=password_2:
            self.add_error('password_2','Two password are not same!')
        
        return self.cleaned_data
        