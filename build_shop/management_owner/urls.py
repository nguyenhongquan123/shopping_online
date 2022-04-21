from django.urls import path,include
from .import views
app_name="management"
urlpatterns = [
    path('',views.index),
    path('1/',views.id),
    path('dashboard/',views.Dashboard.as_view(),name='dashboard'),
]