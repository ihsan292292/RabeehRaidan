from django.urls import path,include
from .views import *

urlpatterns = [
    path('',AdminLoginView.as_view(), name='admin-login')
]