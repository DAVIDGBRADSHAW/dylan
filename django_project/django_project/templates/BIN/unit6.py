python manage.py startapp users
INSTALLED APPS LIST
in settings.py.

The path to setting.py is django_project -> settings.py
Open the file and the list should contain the following

INSTALLED_APPS = [
    "blog.apps.BlogConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

name open apps.py in users -> app.py. You will see the following code.

class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

4. Update the INSTALLED_APPS list with "users.apps.UsersConfig"


INSTALLED_APPS = [
    "blog.apps.BlogConfig",
    "users.apps.UsersConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

from django.contrib.auth.forms import UserCreationForm


from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


11. Add a Cross Site Request Forgery (CSRF) token. This is required by Django
and adds protection from certain attacks. If you do not have it the form will not work.
Once this is in place we can access the form variable passed in the context of this template.

Open urls.py from django_project.

django_project
├── __init__.py
├── asgi.py
├── settings.py
├── urls.py
└── wsgi.py

Update urls.py to the following

from django.contrib import admin
from django.urls import path, include
from users import views as user_views


-> from users import views as user_views --> imports the views from user as user_views.
It's possible import multiple views so as user_views is specifying the views.

-> path('register/', user_views.register, name='register'), --> Defines the path
so if a user goes to /register the users_views.register will be sent to the register view

17. View the app in the browser. 

-> python manage.py runserver
-> Go to http://127.0.0.1:8000/register

You will now see the form and all of the default details Django gives us out of the box.



18. At this points if we try to use the form nothing will happen bar a redirect. 
In our register view any request that comes in we are creating a blank form and 
rendering it out to the template. With HTTP requests we have different options.
Commonly used are POST and GET.

If we get a POST request we can put a check in place to validate the form information
and if we have a GET request leave the redirect.

Update views.py in users -> views.py

users
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── templates
    │   └── users
    │       └── register.html
    ├── tests.py
    └── views.py
19. Create a flash message. In views.py import messages with the following

from django.contrib import messages


There are multiple messages that can be called.

messages.debug
messages.info
messages.success
messages.warning
messages.error

For now we will us messages.success

Update views.py to the following
"""

if form.is_valid(): --> The nested if statement tests if the form is valid
    username = form.cleaned_data.get('username') --> The validated form data will be in the form.cleaned_data dictionary.
    messages.success(request, f'Account created for {username}!') --> This will display a message if the form data was valid. It will display only once

Refer to https://docs.python.org/3/tutorial/inputoutput.html for f strings

#
#

20. Redirect to the home page if the form is valid.

-> import redirect
-> Add return redirect('blog-home')

Updated code for views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

"""
#
#

25. Create one or two users and check the admin page to see if they have been created.

--> Go to http://127.0.0.1:8000/admin/auth/user/ --> after creating users

#
#

26. Add an new email field to the UserCreationForm. To this we need to create a new file in
our users application directory. users -> forms.py 

users
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations
    │   ├── __init__.py
    ├── models.py
    ├── templates
    │   └── users
    │       └── register.html
    ├── tests.py
    └── views.py


#
#

27. Inside forms.py import the following
"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm #Inheritance Relationship

"""

#
#

28. Create two classes. UserRegistrationForm and Meta. forms.py updated...
"""

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm  #Import added
Install crispyforms
pip install django-crispy-forms
pip install crispy-bootstrap5
"""

#
#

30. Update the styling of the form. We could add Bootstrap classes to forms.py but this is mixing the presentation layer with
the back-end logic. A better approach is to use a third party Django app named crispy forms. This allows you
to use some simple tags for styling. crispy forms works with multiple CSS frameworks.


At this point we need to tell Django that this is an installed app.

Refer to https://django-crispy-forms.readthedocs.io/en/latest/

#
#

31. Open settings.py from django_project

django_project
│  ├── __init__.py
│  ├── asgi.py
│  ├── settings.py
│  ├── urls.py
│  └── wsgi.py

Update the INSTALLED APPS list to the following...
"""

INSTALLED_APPS = [
    "blog.apps.BlogConfig",
    "users.apps.UsersConfig",
    "crispy_forms", #Updated here
    "crispy_bootstrap5", #Updated here
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

#At the bottom of settings.py specify the version of Bootstrap you want crispy forms to use.

#
#

33. Run development server and reload the register form.

--> python manage.py runserver  
--> Go to http://127.0.0.1:8000/register
Notice the updated styling on the form

--> View page source and notice the Bootstrap classes added to the form for styling