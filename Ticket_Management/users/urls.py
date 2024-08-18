from django.urls import path
from .views import login_user,logout_user, register_customer

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/',logout_user, name='logout'),
    path('register-customer/', register_customer, name = 'register-customer'),    
]