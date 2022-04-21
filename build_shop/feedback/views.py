from django.shortcuts import render
from .forms import FeedBackForm
from django.views import View
# Create your views here.

class FeedBackView(View):
    
    def get(self,request):
        form=FeedBackForm()
        return render(request,'feedback/contact.html',{'form':form})

    