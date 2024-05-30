# forms.py
from django.contrib.auth import get_user_model
from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import UserProfile
from django import forms
from django import forms
from django import forms
from django.contrib.auth.forms import PasswordResetForm
from .models import CustomUser
from django import forms

class AdminRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'user_type',)

class ManagerRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'user_type',)

class AgentRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'user_type',)

class GuestRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'user_type',)
        

class SignUpForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    
    name = forms.CharField(label='name', max_length=100)
    
    phone_no = forms.CharField(max_length=20)
    
    address = forms.CharField()

    

    class Meta:
        model = User
        fields = ['username',     'email', 
                  
                  'password1', 'password2',  'name',  'phone_no', 'address' ]
        

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2



class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class PasswordResetForm(forms.Form):
    email = forms.EmailField()

from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']











