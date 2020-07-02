Django Authentication

#### Project Setup
1) Setup virtual environment

~~~ bash
python3 -m venv v_auth
~~~

2) Activate virtual environment

~~~ bash
source v_auth/bin/activate
~~~

- `pip freeze` should show nothing since only virtual env was created, nothing installed

3) Install Django

- within virtual environment activated...
- 
~~~ bash
pip install django
~~~

4) Create my_site directory, cd into `my_site`, and then create `my_site` project in that directory. The `.` at the end installs everything in the current directory

~~~ bash
django-admin startproject mysite .
~~~

5) Test that server launches by running `python manage.py runserver` and running port `http://127.0.0.1:8000/`
- ignore migration error messages

6) Run `python manage.py migrate` to apply initial migrations 

7) Create an admin superuser so that the admin panel can be accessed
- Run  `python manage.py createsuperuser`
- leaving Username blank just uses current user

8) Verify admin panel can be reached by going to `http://127.0.0.1:8000/admin/`

#### App Setup

1) Create the `authenticate` app from within virtual environment

    ~~~ bash
    python manage.py startapp authenticate
    ~~~

2) Add `authenticate` app to the `INSTALLED_APPS` section of `settings.py`

    ~~~ py
    INSTALLED_APPS = [
        'authenticate',
        'django.contrib.admin',
        'django.contrib.auth',
    ~~~

3) Create a `urls.py` inside the `authenticate` folder

    ~~~ py
    from django.urls import path

    urlpatterns = [
        path(),
    ]
    ~~~

4) Add a link to the app `urls.py` into the project `urls.py`
   - add the `include` import
   - add a path to the authenticate root directory ( we do not need '/')

   ~~~ py
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('authenticate.urls'))
   ]
   ~~~

#### Build Home page

1) Create directory structure `authenticate/templates/authenticate`

2) Add `home.html`
- this is very basic just to make sure it is set up correctly

    ~~~ html
    <h1> Home page here </h1>
    ~~~

3) Update `views.py`

    ~~~ py
    from django.shortcuts import render

    # Create your views here.
    def home(request):
        return render(request, 'authenticate/home.html', {})
    ~~~

4) Update `urls.py` in `authenticate` app

    ~~~ py
    from django.urls import path
    from . import views

    urlpatterns = [
    path('', views.home, name = "home") 
    ]
    ~~~

5) Update `urls.py` in `my_site` project

    ~~~ py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('authenticate.urls'))
    ]
    ~~~

6) Create `base.html` inside `authenticate` folder
   - a large part of this is copied from the `starter` template at <a href = "https://getbootstrap.com/docs/4.5/getting-started/introduction/" > Bootstrap </a>
   ~~~ html
   <!doctype html>
   <html lang="en">
     <head>
       <!-- Required meta tags -->
       <meta charset="utf-8">
       <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

       <!-- Bootstrap CSS -->
       <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">

       <title>Hello, world!</title>
     </head>
     <body>
    <br/>
    <div class = "container">
        {% block content %}
        {% endblock %}
    </div>

       <!-- Optional JavaScript -->
       <!-- jQuery first, then Popper.js, then Bootstrap JS -->
       <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
       <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
       <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
     </body>
   </html>
   ~~~

7) Update the `home.html` to use the `base.html`   

    ~~~ py
    {% extends 'authenticate/base.html'%}
    {% block content %}

    <h1> Home page here </h1>

    {% endblock %}
    ~~~

#### Building Navbar

- any page that extends `base.html` will contain the navbar

1) Add the following to `base.html`

    - note that dark mode is used in the `nav` tag

        ~~~ html
            <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                <a class="navbar-brand" href="#">Navbar</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav mr-auto">
                        <li class="nav-item active">
                            <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Link</a>
                        </li>
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            Dropdown
                            </a>
                            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                            <a class="dropdown-item" href="#">Action</a>
                            <a class="dropdown-item" href="#">Another action</a>
                            <div class="dropdown-divider"></div>
                            <a class="dropdown-item" href="#">Something else here</a>
                            </div>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link disabled" href="#" tabindex="-1" aria-disabled="true">Disabled</a>
                        </li>
                    </ul>
                    <form class="form-inline my-2 my-lg-0">
                    <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
                    </form>
                </div>
            </nav>
        ~~~

    - full navbar

        <img src = "Bootstrap_navbar_full.png"/>

    - responsive collapsed

        <img src = "Bootstrap_navbar_min_collapsed.png" width = "50%"/>

        - responsive with expanded
        - notice that the button outline persists 

        <img src = "Bootstrap_navbar_min_open.png" width = "50%"/>

2) Override the button outline of `Bootstrap` using the added `static file` 

   - create a new css file `static/css/custom.css` within the `authentication` app
     
   - add to `custom.css`

   ~~~ css
        .buttonOutline button {
            outline-style: none;
        }

        body {
            background: lightgray;
   ~~~

    - add to the top of `base.html`
        - this tells `Django` to look for any static files

    ~~~ html
        {% load static %}
    ~~~

    - add to the bottom of the `head` section of `base.html`

    ~~~ html
            <!-- Custom CSS to override Bootstrap -->
            <link href = "{% static "css/custom.css"%}" rel = "stylesheet">
        </head>
    ~~~

3) Modify navbar to show `Authentication` and the `disabled link`

   - note that there are 2 ways we can comment out sections of code

        - `traditional HTML comment notation` 
        ~~~ html
            <!--
            <li class="nav-item active">
                <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
            </li>
            -->
        ~~~

        - `Dango template tags` that also allow a note to added for further info

        ~~~ html
            {% comment "note explaining why this code is disabled" %} <form class="form-inline my-2 my-lg-0">
            <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Search</button>
            </form> {% endcomment %}
        ~~~

    - modify `Navbar` link

        - name of link is changed
        - link points to `home` as it is referenced in `urls.py` in the app `path('', views.home, name = "home")`

        ~~~ html
        <a class="navbar-brand" href = " {% url 'home' %}">Django Authentication</a>
        ~~~

    - rename `Disabled` link and have move it be on right side of nav bar be changing `mr-auto` to `ml-auto`

        ~~~ html
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item">
                    <a class="nav-link" href = "{% url 'login' %}">Login</a>
                </li>        
        ~~~


    - the nav bar should now look like this

    <img src = "Modified_navbar.png">

#### Login Form

1) Add the following imports into `urls.py` of the app

    ~~~ py
    from django.shortcuts import render
    from django.contrib.auth import authenticate, login, logout

    # Create your views here.
    def home(request):
        return render(request, 'authenticate/home.html', {})
    ~~~

2)  Add a basic `login_user` function to direct user to a login page

    ~~~ py
    def login_user(request):
        return render(request, 'authenticate/login.html', {})  
    ~~~

3) Add a basic `login.html` page to verify view

    ~~~ html
    {% extends 'authenticate/base.html'%}
    {% block content %}

    <h1> Login page here </h1>

    {% endblock %}
    ~~~

4) Update the `urls.py` in the app to add the path(route) to the login page

    ~~~ py
        from django.urls import path
        from . import views

        urlpatterns = [
        path('', views.home, name = "home"),
        path('login/', views.login_user, name = "login"), 
        ]
    ~~~

5) Create form in the `login.html` page

    ~~~ html
    {% extends 'authenticate/base.html'%}
    {% block content %}

    <h2 class = "text-center"> Login page here </h2>

    <div class = "col-md-6 offset-md-3">
        <form>
        <div class="form-group">
            
            <input type="email" class="form-control" aria-describedby="emailHelp" placehiolder = "Enter Username" name = "username">
        
        </div>
        <div class="form-group">
            
            <input type="password" class="form-control" placeholder = "Enter Password" name = "password">
        </div>

        <button type="submit" class="btn btn-primary">Login</button>
        </form>
    </div>

    {% endblock %}
    ~~~

6) Make form functional

   - add a `POST` method to the `form` tag
   - add a `csrf token` for security (prevents cross-site-request-forgery)
   - 

   ~~~ html
       <form> method = "POST">
       {% csrf_token %}
   ~~~

7) Update view to handle login

    - makes sure to import `redirect` at top

    ~~~ py
    from django.shortcuts import render, redirect
    ~~~

   - a registered user(e.g. admin) is redirected to the home page
   - if user does not exist, it keeps user on the login page
   - note, that after admin logs in , the `navbar` still shows `login`
   
   ~~~ py
   def login_user(request):
       if request.method == 'POST':
           username = request.POST['username']
           password = request.POST['password']
           # build user obj
           user = authenticate(request, username=username, password=password)

           # verify if user exists
           if user is not None:
               login(request, user)
               return redirect('home')   # take user to home page  

           else:
               return redirect('login') # stay on the login page

       else:
           return render(request, 'authenticate/login.html', {})
   ~~~

#### Add some messages for login & logout process

1) Update `views.py` of the app

    - import `messages` in `views.py` of the app

       ~~~ py
       from django.contrib import messages
       ~~~

    - update the `login_user` method

    ~~~ py
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
    ~~~

    - create a `logout_user` method

    ~~~ py
        def logout_user(request):
        logout(request)
        messages.success(request, "You are logged out" )
        return redirect('home')   # take user to home page
    ~~~

2) Add the following to `base.html`

    ~~~ html
        
                    {% if  user.is_authenticated %}
                        <a class="nav-link" href = "{% url 'logout' %}">Logout</a>
                    {% else %}
                    <li class="nav-item">   
                        <a class="nav-link" href = "{% url 'login' %}">Login</a>
                            
                    </li>

                    {% endif %}
                </ul>
            </div>
        
        </nav>    



        <br/>
        <div class = "container">
            {% if messages %}
                {% for message in messages %}
                    <div class="alert alert-dark alert-dismissable" role="alert">
                        <button class = "close" data-dismiss = "alert" >
                            <small><sup>x</sup></small>
                        </button>
                        {{ message }}
                    </div>
                {% endfor %}    

            {% endif %}

            {% block content %}
            {% endblock %}
        </div>
    ~~~

3) Update the `urls.py` of the app

    ~~~ py
    from django.urls import path
    from . import views

    urlpatterns = [
    path('', views.home, name = "home"),
    path('login/', views.login_user, name = "login"),
    path('logout/', views.logout_user, name = "logout"), 
    ]
    ~~~

#### Modify home page to show user info when logged in
1) Update `home.html`

    ~~~ html
    {% if user.is_authenticated %}
        <p> User: {{user.username}} </p>
        <p> email: {{ user.email}}</p>
        <p> name: {{user.first_name}} {{user.last_name }} </p>
    {% endif %}
    ~~~

#### User Registration Setup

1) Create `register_user` method in `views.py` in app

   - a simple route to registration page is put together to make sure app is wired up correctly
 
    ~~~ py
    def register_user(request):
        return render(request, 'authenticate/register.html', {})
    ~~~

2) Add a register link to `base.html`

    ~~~ html
        <li class="nav-item">   
            <a class="nav-link" href = "{% url 'login' %}">Login</a>                       
        </li>
        <li class="nav-item">   
            <a class="nav-link" href = "{% url 'register' %}">Register</a>                       
        </li>
    ~~~


3) Update `urls.py` to add route to registration page

    ~~~ py
    from django.urls import path
    from . import views

    urlpatterns = [
    path('', views.home, name = "home"),
    path('login/', views.login_user, name = 'login'),
    path('logout/', views.logout_user, name = 'logout'), 
    path('register/', views.register_user, name = 'register'),
    ]
    ~~~

4) Create a simple `register.html` to verify link works properly

    ~~~ html
    {% extends 'authenticate/base.html' %}

    {% block content %}
        <h2> Register page </h2>

    {% endblock %}
    ~~~

#### Registration form using Django's built in tools 

1) Update `register_user` method to use Django's `UserCreationForm`

   - add import for `UserCreationForm` in `views.py`

   ~~~ py
   from django.shortcuts import render, redirect
   from django.contrib.auth import authenticate, login, logout
   from django.contrib import messages
   from django.contrib.auth.forms import UserCreationForm
   ~~~

   - update the `register_user` method

    ~~~ py
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
    ~~~

    - create a registration form in `register.html`

2) Update `register.html` to include a form to pass data into view

    ~~~html
    {% extends 'authenticate/base.html' %}

    {% block content %}
        <h2> Register page </h2>

        <form method = "POST" action = "{% url 'register' %}">
            {% csrf_token %}
            
            {% if form.errors%}
                <p> Error in form </p>
            {% endif %}
        
            {{ form.as_p }}

            <input type = "submit" value = "Register" class = " btn btn-secondary">
        </form>
    {% endblock %}
    ~~~

#### Creating Registration form manually

1) Create `forms.py` in the app's  `authenticate` folder

   - import the following

   ~~~ py
   from django.contrib.auth.forms import UserCreationForm
   from django import forms
   from django.contrib.auth.models import User
   ~~~

   - create the `SignUpForm` class

   ~~~ py
   class SignUpForm(UserCreationForm):
       email = forms.EmailField()
       first_name = forms.CharField(max_length = 50)
       last_name = forms.CharField(max_length = 50)

       class Meta:
           model = User
           fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
   ~~~

2) Update `views.py`

   - add import 

   ~~~ py
   from .forms import SignUpForm
   ~~~

- replace `UserCreationForm` with `SignUpForm` in the `register_user` method

    ~~~ py
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
    ~~~

3) Center the `form` tag in `register.html` by surrounding it with the following 

    ~~~ html
    <div class = "col-md-6 offset-md-3">
    ~~~

4) Center the `h2` tag  by adding a class

    ~~~ html
    <h2 class = "text-center"> Register page </h2>
    ~~~

5) Add widgets to the `email`, `first_name`, `last_name` properties of the `SignUpForm` class

    ~~~ py
    class SignUpForm(UserCreationForm):
        email = forms.EmailField( widget = forms.TextInput(attrs={'class': 'form-control'})) 
        first_name = forms.CharField(max_length = 50, widget = forms.TextInput(attrs={'class': 'form-control'}))
        last_name = forms.CharField(max_length = 50, widget = forms.TextInput(attrs={'class': 'form-control'}))
    ~~~

6) Update the `username`, `password1`, and `password2` properties using the bootstrap `form-control` class

    ~~~ py
        class Meta:
            model = User
            fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, *kwargs)

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['class'] = 'form-control'  
            self.fields['password2'].widget.attrs['class'] = 'form-control''
    ~~~

7) Add placeholders for each field and remove the labels

    ~~~ py
    class SignUpForm(UserCreationForm):
        email = forms.EmailField( label = '', widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})) 
        first_name = forms.CharField(label = '', max_length = 50, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
        last_name = forms.CharField(label = '', max_length = 50, widget = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

        class Meta:
            model = User
            fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, *kwargs)

            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['username'].widget.attrs['placeholder'] = 'User Name'
            self.fields['username'].label = ''

            self.fields['password1'].widget.attrs['class'] = 'form-control'  
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password1'].label = ''

            self.fields['password2'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
            self.fields['password2'].label = ''
    ~~~

8) Added `Help Text` to the `username`, `password1`, and `password2` fields

~~~ py
def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, *kwargs)

        # user_msg = "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only"
        user_msg = '<span class = "form-text text-muted"><small> Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only </small> </span>'

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        # self.fields['username'].help_text = '<span class = "form-text text-muted"><small> Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only </small> </span>'
        self.fields['username'].help_text = user_msg

        self.fields['password1'].widget.attrs['class'] = 'form-control'  
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class = "form-text text-muted"> <li>Your password can’t be too similar to your other personal information</li> <li> Your password must contain at least 8 characters </li> <li> Your password can’t be a commonly used password </li> <li>Your password can’t be entirely numeric</li> </ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class = "form-text text-muted"><small> Enter the same password as before, for verification </small> </span>'
~~~


