from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUserModel

class UserRegistrationForm(UserCreationForm):

    user_fname = forms.CharField(max_length=100, label="First name")
    user_mname = forms.CharField(max_length=100, label="Middle name", required=False)
    user_lname = forms.CharField(max_length=100, label="Last name")
    user_email = forms.CharField(max_length=100, label="User E-mail")

    class Meta:
        model = CustomUserModel
        fields = ['user_fname', 'user_mname', 'user_lname', 'user_email']


class UserLoginForm(forms.ModelForm):

    user_email = forms.EmailField(max_length=300, label="User-Email")
    
    class Meta:
        model = CustomUserModel
        fields = ['user_email',]