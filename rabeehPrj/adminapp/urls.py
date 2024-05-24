from django.urls import path,include
from .views import *

urlpatterns = [
    path('',admin_login,name='admin-login'),
    path('admin-home',index,name='index')
]