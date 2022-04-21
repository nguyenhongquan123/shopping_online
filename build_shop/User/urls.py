from django.urls import path,include
from .import views
app_name="user"
urlpatterns = [
    path('addDelivery/',views.CreateDelivery.as_view(),name="add_delivery"),
]