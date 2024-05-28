from django.urls import path,include
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('cart/',cart_view,name='cart')
]