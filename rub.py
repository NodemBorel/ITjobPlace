'''
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]


=================================================================================================================

from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

===================================================================================================================

    from django.shortcuts import render, redirect
    from .forms import RegistrationForm, LoginForm
    from .models import User
    
    def register(request):
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = User(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            form = RegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})
    
    def user_login(request):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                try:
                    user = User.objects.get(username=username)
                    if user.check_password(password):
                        request.session['user_id'] = user.id
                        return redirect('home')  # Change 'home' to the name of your homepage URL pattern
                    else:
                        form.add_error(None, 'Invalid username or password')
                except User.DoesNotExist:
                    form.add_error(None, 'Invalid username or password')
        else:
            form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})
    
    def user_logout(request):
        del request.session['user_id']
        return redirect('login')

        
==================================================================================================================      
        from django.db import models
        from django.contrib.auth.hashers import make_password, check_password
        
        class User(models.Model):
            username = models.CharField(max_length=150, unique=True)
            email = models.EmailField(unique=True)
            password = models.CharField(max_length=128)
        
            def save(self, *args, **kwargs):
                # Hash the password before saving
                self.password = make_password(self.password)
                super().save(*args, **kwargs)
        
            def check_password(self, raw_password):
                return check_password(raw_password, self.password)
=============================================================================================================
'''        