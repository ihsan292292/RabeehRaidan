from django.urls import path,include
from .views import *

from rest_framework import routers
router = routers.SimpleRouter()

urlpatterns = [
    path('', custom_login_view, name='custom_admin_login'),
    path('logout/',custom_logout_view,name="custom_logout_view"),
    path('home/', home_view, name='admin_home'),
    path('forms/',forms, name='forms'),
    path('table/',tables, name="tables"),
    path('product/',product, name="product"),
    path('staff/',staff, name="staff"), 
    path('branches/',branch, name="branch"),
    path('offers/',offers, name="offers")
]