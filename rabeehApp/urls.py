<<<<<<< HEAD:rabeehApp/urls.py
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',index)
=======
from django.urls import path
from .views import *

urlpatterns = [
  path('',index,name='index'),
>>>>>>> main:rabeehPrj/rabeehApp/urls.py
]