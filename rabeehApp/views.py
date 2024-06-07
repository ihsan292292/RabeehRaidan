from django.shortcuts import render,redirect
from adminapp.models import *
from django.http import HttpResponse

# Create your views here.


# home
def index(request):
    return render(request,'home/index.html')

# customer reg
def register_customer(request):
    if request.method == 'POST':
        # Extracting user data from the POST request
        username = request.POST.get('username')
        phone = request.POST.get('phone')

        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            # If user exists, redirect to product display
            return redirect('productdisplay')
        
        # Creating a new User instance
        user = User.objects.create_user(username=username)
        
        # Creating a new Customer instance
        customer = Customer(user=user, phone=phone)
        customer.save()
        return redirect('productdisplay')
    else:
        return redirect('index')
# productdisplay    
def productdisplay(request):
    product = Product.objects.all()
    branches = Branch.objects.all()
    context = {'product':product,
               'branches':branches}
    return render(request,'product/productdisplay.html',context)
        
def cart_view(request):
    return render(request,'cart/cart.html')