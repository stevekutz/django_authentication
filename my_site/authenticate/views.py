from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'authenticate/home.html', {})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # build user obj
        user = authenticate(request, username=username, password=password)

        # verify if user exists
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in" )
            return redirect('home')   # take user to home page  

        else:
            messages.success(request, "Error not logged in" )
            return redirect('login') # stay on the login page

    else:
        return render(request, 'authenticate/login.html', {})  


def logout_user(request):
    logout(request)
    messages.success(request, "You are logged out" )
    return redirect('home')   # take user to home page