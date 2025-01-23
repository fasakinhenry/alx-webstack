from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from serviceproviders.models import Profile as ServiceProviderProfile
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout as auth_logout
from .forms import UserRegistrationForm, ProfileEditForm
from rest_framework import generics
from .serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Profile

# Home page view
def home(request):
    """Render the home page."""
    # if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
    #    return JsonResponse({'message': 'Welcome to the home page'})
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
            profile.save()

            messages.success(request, f'Account created for {user.username}!')
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
                return JsonResponse({'message': f'Account created for {user.username}!'})
            return redirect('login')
    else:
        form = UserRegistrationForm()

    # if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
    #  return JsonResponse({'form': form.errors})
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
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
                return JsonResponse({'message': 'Login successful'})
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

# User logout view
def logout(request):
    """Logout the user and redirect to the home page."""
    auth_logout(request)
    # if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
    #    return JsonResponse({'message': 'Logout successful'})
    return redirect('home')

# Dashboard view
@login_required
def dashboard(request):
    """Render the dashboard page."""
    # if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
    #    return JsonResponse({'message': 'Welcome to the dashboard'})
    return render(request, 'dashboard.html')

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
            #if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
            #    return JsonResponse({'message': 'Profile updated successfully.'})
            return redirect('profile_view')
    else:
        form = ProfileEditForm(instance=profile)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
        return JsonResponse({'form': form.errors})
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
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
            return JsonResponse({'error': 'Please complete your profile.'})
        return redirect('edit_profile')

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
       return JsonResponse({'profile': {
          'username': profile.user.username,
          'bio': profile.bio,
          'phone_number': profile.phone_number,
          'skills': profile.skills,
          'profile_picture': profile.profile_picture.url if profile.profile_picture else None
         }
       })
    return render(request, 'profile_view.html', {'profile': profile})


@login_required
def view_users(request):
    """Render the view users page."""
    profiles = Profile.objects.select_related('user').all()
    return render(request, 'view_users.html', {'profiles': profiles})

# About page view
def about(request):
    """Render the about page."""
    # if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
#        return JsonResponse({'message': 'Welcome to the about page'})
    return render(request, 'about.html')

# Jobs page view
@ login_required
def jobs(request):
    """Render the jobs page."""
    # if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
        # return JsonResponse({'message': 'Welcome to the jobs page'})
    return render(request, 'jobs.html')

# Tables page view
@ login_required
def tables(request):
    """Render the tables page."""
    # if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
    #    return JsonResponse({'message': 'Welcome to the tables page'})
    return render(request, 'tables.html')

# Freelancer page view
@ login_required
def freelancer(request):
    """Render the freelancer page."""
    profiles = ServiceProviderProfile.objects.all()
    return render(request, 'freelancer.html', {'profiles': profiles})

# Employees page view
# @ login_required
# def employees(request):
#    """Render the employees page."""
#    return render(request, 'employees.html')

# All users page view
@ login_required
def allusers(request):
    """Render the all users page."""
    profiles = Profile.objects.all()
    return render(request, 'allusers.html', {'profiles': profiles})


@ login_required
def profiles_api(request):
    """API view to return profiles data as JSON."""
    profiles = Profile.objects.select_related('user').all()
    profiles_data = [
        {
            'id': profile.id,
            'username': profile.user.username,
            'bio': profile.bio,
            'phone_number': profile.phone_number,
            'skills': profile.skills,
            'profile_picture': profile.profile_picture.url if profile.profile_picture else None
        }
        for profile in profiles
    ]
    return JsonResponse(profiles_data, safe=False)

# API view for profiles
class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

class ProfileDetailAPIView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

