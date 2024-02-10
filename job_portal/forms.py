from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered.")
        
        # Check if passwords match
        if password != confirm_password:
            raise forms.ValidationError("The passwords do not match.")         

class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'salary', 'job_type', 'Job_Description', 'link']
