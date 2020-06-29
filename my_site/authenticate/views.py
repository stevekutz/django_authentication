from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

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

def register_user(request):
    # if user types info into form, create form obj from request data
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # extract out username & password
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have successfully registered"))
            return redirect('home')


    # if user did not type in anything
    else: 
        form = UserCreationForm()

    # create a context dictionary
    context = {'form': form}

    return render(request, 'authenticate/register.html', context)