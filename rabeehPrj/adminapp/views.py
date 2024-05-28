from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def custom_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to 'home/index.html'
        else:
            return HttpResponse('Invalid login credentials')
    return render(request, 'login.html')


def home_view(request):
    return render(request, 'index.html')

def forms(request):
    return render(request,'forms.html')

def tables(request):
    return render(request,'tables.html')

# ///////////////////////////////////////////////////

def product(request):
    return render(request,'Product/product.html')

def staff(request):
    return render(request,'Staff/staff.html')

def branch(request):
    return render(request,'Branch/branchs.html')
