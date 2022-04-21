from django.urls import path,include
from .import views
from django.contrib.auth.decorators import login_required
app_name='home'
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('login-register/',views.SiteLoginRegister.as_view(),name='login-register'),
    path('logout/',views.logout_function,name="logout"),  
    path('cc/',views.regis.as_view(),name="cc"),
    # path("dashboard/",views.dashboard,name="dashboard"),
    #  path("dashboard/",views.vdashboard.as_view(),name="dashboard"),
]

