from django.shortcuts import render,redirect
from adminapp.models import *
from .models import *
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404

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
    if request.method == 'POST':
        branch_id = request.POST.get('branch_id')
        product = Product.objects.filter(branch__id=branch_id)
        branches = Branch.objects.all()
        selected_branch_id = request.POST.get('branch_id', 'all') 
        context = {'product':product,
                   'selected_branch_id': selected_branch_id,
                    'branches':branches}
        return render(request,'product/productdisplay.html',context) 
    else:
        product = Product.objects.all()
        branches = Branch.objects.all()
        selected_branch_id = request.POST.get('branch_id', 'all') 
        context = {'product':product,
                   'selected_branch_id': selected_branch_id,
                    'branches':branches}
        return render(request,'product/productdisplay.html',context)

def filter_products(request,id):
    branch_id = request.GET.get('branch_id')
    print('Branch ID:', branch_id)
    if branch_id == 'all':
        products = Product.objects.all()
    else:
        products = Product.objects.filter(branch__id=branch_id)       

    return render(request, 'partials/product_partial_list.html', {'product': products})

def add_cart(request,id):
    product = Product.objects.get(id=id)
    count=1
    c = Cart(name=product.name,price=product.price,branch=product.branch,image=product.image,prod_id=id,qty=count)
    c.save()
    return redirect('productdisplay')

def delete_cart(request,id):
    a = Cart.objects.get(id=id)
    a.delete()
    return redirect(cart_view)

def cartinc(request,id):
    a = Cart.objects.get(id=id)
    b = Product.objects.get(id=a.prod_id)#main product model
    a.qty += 1
    a.price = b.price * a.qty
    a.save()
    return redirect(cart_view)

def cartdec(request, id):
    cart_item = get_object_or_404(Cart, id=id)
    product = get_object_or_404(Product, id=cart_item.prod_id)
    
    if cart_item.qty > 0:
        cart_item.qty -= 1
        cart_item.price = product.price * cart_item.qty
        cart_item.save()
        
        # If the quantity becomes zero, handle accordingly
        if cart_item.qty == 0:
            cart_item.delete()  # Remove the item from the cart
            return redirect(cart_view)
        
    return redirect(cart_view)

def cart_view(request):
    cart = Cart.objects.all()
    name = []
    tp1 = []
    tp2 = []
    for i in cart:
        name.append(i.name)
        tp1.append(i.price)
    for j in tp1:
        tp2.append(int(j))

    item_count = len(name)   
    total_price = sum(tp2)
    context = {'product':cart,
               "total":total_price,
               "item_count":item_count}
    return render(request,'cart/cart.html',context)