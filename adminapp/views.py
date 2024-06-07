from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from django.contrib.auth.models import Group


def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # First try to authenticate as a normal user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            request.session['user'] = user.username
            login(request, user)
            return redirect('admin_home')  # Redirect to the admin home page
        else:
            # If normal authentication fails, try to authenticate as a staff member using the phone as the password
            try:
                staff = Staff.objects.get(user__username=username, phone=password)
                user = staff.user
                request.session['user'] = user.username
                login(request, user)
                return redirect('admin_home')  # Redirect to the staff home page
            except Staff.DoesNotExist:
                # If staff authentication also fails, show an error message
                messages.error(request, 'Invalid login credentials')
    
    return render(request, 'login.html')

# logout
def custom_logout_view(request):
    logout(request)
    return redirect('custom_admin_login')


# index
def home_view(request):

    
    return render(request, 'index.html')

def forms(request):
    return render(request,'forms.html')

def tables(request):
    return render(request,'tables.html')

# ///////////////////////////////////////////////////

# PRODUCT CRUD
def product(request):
    prds = Product.objects.all()
    branches = Branch.objects.all()
    if request.method == "POST" and 'name' in request.POST and 'price' in request.POST and not 'product_id' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        branch_id = request.POST.get('branch')
        branchi = Branch.objects.get(id=branch_id)
    
        prd = Product(name=name, price=price,branch=branchi)
        prd.save()
        messages.success(request, f'{name} Added Successfully!')
    elif request.method == "POST" and 'product_id' in request.POST:
        product_id = request.POST.get('product_id')
        if 'name' in request.POST and 'price' in request.POST:
            # Update product
            name = request.POST.get('name')
            price = request.POST.get('price')
            prd = Product.objects.get(id=product_id)
            prd.name = name
            prd.price = price
            prd.branch = branch
            prd.save()
            messages.success(request, f'{name} Updated Successfully!')
        else:
            # Delete product
            prd = Product.objects.get(id=product_id)
            prd.delete()
            messages.success(request, f'Product Deleted Successfully!')
        return redirect('product')

    context = {
        'prds': prds,
        'branches':branches
    }
    return render(request, 'Product/product.html', context=context)

# Staff CRUD
def staff(request):
    staff_members = Staff.objects.all()
    branches = Branch.objects.all()

    if request.method == "POST":
        if 'username' in request.POST and 'password' in request.POST and not 'staff_id' in request.POST:
            # Add staff
            username = request.POST.get('username')
            password = request.POST.get('password')
            phone = request.POST.get('phone')
            branch_id = request.POST.get('branch')
            branch = Branch.objects.get(id=branch_id)
            
            # Check if user already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Staff with username {username} already exists!')
            else:
                user = User.objects.create_user(username=username, password=password)
                print("User Name ::", user.username)
                staff = Staff(user=user, phone=phone, branch=branch)
                staff.save()
                messages.success(request, f'{username} Added Successfully!')
        
        elif 'staff_id' in request.POST:
            staff_id = request.POST.get('staff_id')
            if 'username' in request.POST and 'phone' in request.POST and 'branch' in request.POST:
                # Update staff
                username = request.POST.get('username')
                phone = request.POST.get('phone')
                branch_id = request.POST.get('branch')
                branch = Branch.objects.get(id=branch_id)
                staff = Staff.objects.get(id=staff_id)
                
                # Check if the username is being changed and if the new username already exists
                if staff.user.username != username and User.objects.filter(username=username).exists():
                    messages.error(request, f'Staff with username {username} already exists!')
                else:
                    staff.user.username = username
                    staff.user.save()
                    staff.phone = phone
                    staff.branch = branch
                    if 'password' in request.POST and request.POST.get('password'):
                        staff.user.set_password(request.POST.get('password'))
                        staff.user.save()
                    staff.save()
                    messages.success(request, f'{username} Updated Successfully!')
            else:
                # Delete staff
                staff = Staff.objects.get(id=staff_id)
                staff.delete()
                messages.success(request, f'Staff Deleted Successfully!')
            return redirect('staff')

    context = {
        'staff_members': staff_members,
        'branches': branches,
    }
    return render(request, 'Staff/staff.html', context=context)


# BRANCH CRUD
def branch(request):
    branches = Branch.objects.all()
    if request.method == "POST":
        if 'branch_id' in request.POST:
            branch_id = request.POST.get('branch_id')
            br = Branch.objects.get(id=branch_id)

            if 'location' in request.POST and 'phone' in request.POST and 'map' in request.POST:
                # Update branch
                br.location = request.POST.get('location')
                br.phone = request.POST.get('phone')
                br.gmap = request.POST.get('map')
                br.save()
                messages.success(request, f'Branch at {br.location} Updated Successfully!')
            else:
                # Delete branch
                br.delete()
                messages.success(request, 'Branch Deleted Successfully!')
        else:
            # Add new branch
            location = request.POST.get('location')
            phone = request.POST.get('phone')
            map = request.POST.get('map')
            br = Branch(location=location, phone=phone, gmap=map)
            br.save()
            messages.success(request, f'Branch at {location} Added Successfully!')
        return redirect('branch')  # replace 'branch' with the name of your branch URL pattern

    context = {
        'branches': branches
    }
    return render(request, 'Branch/branchs.html', context=context)


def offers(request):
    return render(request,'Product/offers.html')
