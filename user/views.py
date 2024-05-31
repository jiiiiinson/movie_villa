from django.contrib import messages
from django.shortcuts import render, redirect
from movies.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as django_logout
from .models import SignUpForm, ProfileForm, Profile
from django.core.exceptions import SuspiciousOperation
from authentication.models import *


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful! Welcome to Movie Villa')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form, 'errors': form.errors})


def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        try:
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                auth_login(request, user)
                return redirect('home')
        except SuspiciousOperation:
            return render(request, 'login.html')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    django_logout(request)
    return redirect('home')


def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})
