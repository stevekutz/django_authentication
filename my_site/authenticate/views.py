from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages

from .forms import SignUpForm, UserEditForm


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
        form = SignUpForm(request.POST)
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
        form = SignUpForm()

    # create a context dictionary
    context = {'form': form}

    return render(request, 'authenticate/register.html', context)

def edit_profile(request):

    if request.method == 'POST':
            form = UserEditForm(request.POST, instance = request.user)
            if form.is_valid():
                form.save()
        
                messages.success(request, ("You have updated your profile"))
                return redirect('home')


    # if user did not type in anything
    else: 
        form = UserEditForm(instance = request.user)

    # create a context dictionary
    context = {'form': form}

    return render(request, 'authenticate/edit_profile.html', context)   


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data = request.POST, user = request.user)
        if form.is_valid():
            form.save()
            # this keep user logged in after changing password 
            update_session_auth_hash(request, form.user)   

            messages.success(request, ("You have changed your password"))
            return redirect('home')


    # if user did not type in anything
    else: 
        form = PasswordChangeForm(user = request.user)

    # create a context dictionary
    context = {'form': form}

    return render(request, 'authenticate/change_password.html', context) 