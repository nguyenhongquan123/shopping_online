from django.urls import path
from .import views

app_name='cart'
urlpatterns = [
    path('',views.DetailCart.as_view(), name="detail_cart"),
    path('delete/<str:product_id>/',views.deleteProductCart,name="delete_product_cart"),
    path('product_detail/<slug:slug>/',views.AddProductCart.as_view(),name='add_product_cart'),
    path('post_comment/>',views.post_Comment,name='post_comment'),
    path('test/',views.test.as_view()),
]

