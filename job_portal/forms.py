from django.forms import ModelForm
from django import forms
from .models import *


class RegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    email = forms.CharField(widget=forms.EmailInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered.")

        if not password or len(password) < 6:
            raise ValidationError("Password must be at least 6 characters long.")
        
        # Check if passwords match
        if password != confirm_password:
            raise forms.ValidationError("The passwords do not match.")    
        
class JobForm(ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'salary', 'job_type', 'Job_Description', 'link']
