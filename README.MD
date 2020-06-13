Django Authetication

#### Setup
1) Setup virutal environment

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