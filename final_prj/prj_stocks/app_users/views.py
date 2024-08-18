from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import CustomUserModel
from .forms import UserRegistrationForm, UserLoginForm

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate

"""
View: Index Page
Success: Index page successful load --> Welcome Page view
Failure: Index page unsuccessful --> Redirected to Failure to load Welcome Page view
"""

def indexView(request):
    return render(request, "index.html")


"""
View: Login/Sign-In Form
Success: Login successful --> Dashboard view
Failure: Login unsuccessful --> Redirected to Login View
"""

def dashboardView(request):
    return render(request, "dashboard.html")


"""
View: Registration Form
Success: Registration successful --> Confirmation E-mail sent view
Failure: Registration unsuccessful --> Redirected to Registration View
"""

def registerPleaseView(request):

    if request.method == "GET":
        registration_form = UserRegistrationForm(request.GET)
        return render(request, 'registration.html', {'form': registration_form})


    elif request.method == "POST":
        form_data = request.POST
        if form_data:
            user_obj = CustomUserModel()
            user_obj.user_fname = form_data.get('user_fname')
            user_obj.user_mname = form_data.get('user_mname')
            user_obj.user_lname = form_data.get('user_lname')
            user_obj.user_email = form_data.get('user_email')
            user_obj.is_customer = True
            user_obj.save()            
            return render(request, "registration_successful.html")
        else:
            return render(request, "registration_failure.html")


"""
View: Login Form
Success: Login successful --> Enter dashboard
Failure: Login unsuccessful --> Redirected to Login View
"""

def loginPleaseView(request):

    if request.method == "GET":
        login_form = UserLoginForm(request.GET)
        return render(request, 'login.html', {"form": login_form})

    elif request.method == "POST":
        user_obj = request.POST
        print('abc', request.user, request.POST)
        user_obj_username = user_obj.get('user_email')
        user_obj_password = user_obj.get('password')
        print('user', user_obj_username, user_obj_password)
        user_is_authenticated = authenticate(user_email=user_obj_username, password=user_obj_password)
        print('auth', user_is_authenticated)
        if user_is_authenticated:
            return render(request, 'dashboard.html')
        else:
            return render(request, 'login_failure.html')
