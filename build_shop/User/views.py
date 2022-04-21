from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView
from .forms import AddDeliveryUserForm
class CreateDelivery(FormView):
    template_name='orders/create_order.html'
    form_class=AddDeliveryUserForm
    def get(self ,request, *args, **kwargs):
        
        return super().get(request, *args, **kwargs)
    def form_valid(self,form):
        # cd=form.cleaned_data
        instance=form.save(commit=False)
        instance.customer=self.request.user.customer
        instance.save()        
        return HttpResponse("thanh cong")
        
        
        