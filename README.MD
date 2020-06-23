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

