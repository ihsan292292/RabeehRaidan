from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SuperuserLoginForm

# Create your views here.


def admin_login(request):
    if request.method == 'POST':
        form = SuperuserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_superuser:  # Ensure the user is a superuser
                login(request, user)
                request.session['user'] = user.username
                return redirect('index')
    else:
        form = SuperuserLoginForm()
    return render(request, 'login.html', {'form': form})

def index(request):
    
    context = {
        'username':request.session['user']
    }
    
    return render(request,'Home/home.html',context=context)

