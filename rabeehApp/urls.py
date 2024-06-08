from django.urls import path,include
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('register_customer/',register_customer,name='register_customer'),
    path('productdisplay/',productdisplay,name='productdisplay'),
    path('students/<int:id>/', filter_products, name='filter_products'),
    path('cart/',cart_view,name='cart'),
    path('add_cart/<int:id>',add_cart,name='add_cart'),
    path('cart_inc/<int:id>',cartinc,name='cart_inc'),
    path('cart_dec/<int:id>',cartdec,name='cart_dec'),
    path('delete_cart/<int:id>',delete_cart,name='delete_cart')
]