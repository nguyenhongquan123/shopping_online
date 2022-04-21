from django import forms

class FeedBackForm(forms.Form):
    email=forms.EmailField()
    message=forms.CharField(widget=forms.Textarea)
    
    
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
        
    