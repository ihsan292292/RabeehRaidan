from django.shortcuts import render

# Create your views here.


# home
def index(request):
    return render(request,'home/index.html')

def cart_view(request):
    return render(request,'home/cart.html')