from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.base import TemplateView
# Create your views here.
def index(request):
    return render(request,'management/base.html')


class Dashboard(UserPassesTestMixin,TemplateView):
    login_url="home:cc"
    template_name="management/dashboard/index.html"
    
    def test_func(self):
        try:
            return self.request.user.is_owner
        except:
            return False
        
    
    # def get(self,request):
    #     return self.render_to_response()
    
def id(request):
    return render(request,'management/dashboard/index1.html')