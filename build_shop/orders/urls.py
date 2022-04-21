from django.urls import path,include
from .import views
app_name="orders"
urlpatterns = [
    path('detail/<slug:slug>/',views.Order_Detail.as_view(),name="order_detail"),
    path('',views.Order_Detail.as_view(),name="order_detail_all"),
    path('create_order/',views.CreateOrder.as_view(),name="create_order"),
    path('validateId',views.validateId,name="validateId"),
    path('cc',views.index),
]