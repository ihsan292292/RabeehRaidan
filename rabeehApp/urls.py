from django.urls import path,include
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('register_customer/',register_customer,name='register_customer'),
    path('productdisplay/',productdisplay,name='productdisplay'),
    path('cart/',cart_view,name='cart')
]