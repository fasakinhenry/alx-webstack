from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from clients.models import Profile
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, ProfileEditForm


# Home page view
def home(request):
    """Render the home page."""
    return render(request, 'home.html')


# User registration view
def register(request):
    """Render the registration page."""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create a Profile instance for the new user
            profile = Profile.objects.create(user=user)
            profile.phone_number = form.cleaned_data.get('phone_number')
            profile.skills = form.cleaned_data.get('skills')
            profile.save()

            messages.success(request, f'Account created for {user.username}!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form': form})


# User login view
def login_view(request):
    """Render the login page."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, 'Both username and password are required.')
            return render(request, 'login.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


# User logout view
def logout_view(request):
    """Logout the user and redirect to the home page."""
    logout(request)
    return redirect('home')


# Dashboard view
@login_required
def dashboard(request):
    """Render the dashboard page."""
    return render(request, 'dashboard.html')


# View users (list of profiles)
def view_users(request):
    """Render a list of all user profiles"""
    profiles = Profile.objects.select_related('user').all()
    return render(request, 'view_users.html', {'profiles': profiles})


# Edit profile view
@login_required
def edit_profile(request):
    """Render the edit profile page."""
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # Create a profile if it does not exist
        profile = Profile.objects.create(user=request.user)

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile_view')
    else:
        form = ProfileEditForm(instance=profile)

    return render(request, 'edit_profile.html', {'form': form})


# Profile view
@login_required
def profile_view(request):
    """Render the profile page."""
    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        # If the profile doesn't exist, redirect to edit profile to create one
        messages.warning(request, 'Please complete your profile.')
        return redirect('edit_profile')

    return render(request, 'profile_view.html', {'profile': profile})
