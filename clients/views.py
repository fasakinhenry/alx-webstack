from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from serviceproviders.models import Profile
from clients.models import Profile as ClientProfile
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm, ProfileEditForm
from rest_framework import generics
from clients.serializers import ProfileSerializer
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
            return redirect('client_login')
    else:
        form = UserRegistrationForm()

    # if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
    #  return JsonResponse({'form': form.errors})
    return render(request, 'client_register.html', {'form': form})

# User login view
def login_view(request):
    """Render the login page."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not username or not password:
            messages.error(request, 'Both username and password are required.')
            return render(request, 'client_login.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
                return JsonResponse({'message': 'Login successful'})
            return redirect('client_dashboard')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'client_login.html')

# User logout view
def client_logout(request):
    """Logout the user and redirect to the home page."""
    logout(request)
    # if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
    #    return JsonResponse({'message': 'Logout successful'})
    return redirect('home')

# Dashboard view
@login_required
def dashboard(request):
    """Render the dashboard page."""
    # if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
    #    return JsonResponse({'message': 'Welcome to the dashboard'})
    return render(request, 'client_dashboard.html')

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
            return redirect('client_profile_view')
    else:
        form = ProfileEditForm(instance=profile)

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
        return JsonResponse({'form': form.errors})
    return render(request, 'client_edit_profile.html', {'form': form})

# Employee profile view
@login_required
def employees(request):
    """Render the employees page."""
    profiles = ClientProfile.objects.all()
    return render(request, 'client_employees.html', {'profiles': profiles})

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
        return redirect('client_edit_profile')

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
#        return JsonResponse({'profile': {
#           'username': profile.user.username,
#            'bio': profile.bio,
#           'phone_number': profile.phone_number,
#           'skills': profile.skills,
#           'profile_picture': profile.profile_picture.url if profile.profile_picture else None
#       }})
        return render(request, 'client_profile_view.html', {'profile': profile})


@login_required
def view_users(request):
    """Render the view users page."""
    profiles = Profile.objects.select_related('user').all()
    return render(request, 'client_view_users.html', {'profiles': profiles})

# About page view
def about(request):
    """Render the about page."""
    # if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
#        return JsonResponse({'message': 'Welcome to the about page'})
    return render(request, 'client_about.html')

# Jobs page view
def jobs(request):
    """Render the jobs page."""
    # if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
        # return JsonResponse({'message': 'Welcome to the jobs page'})
    return render(request, 'jobs.html')

# Tables page view
def tables(request):
    """Render the tables page."""
    # if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or request.GET.get('format') == 'json':
    #    return JsonResponse({'message': 'Welcome to the tables page'})
    return render(request, 'clients_tables.html')

# Freelancer page view
def freelancer(request):
    """Render the freelancer page."""
    return render(request, 'freelancer.html')



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


#messages/chat

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message, Profile
from django.contrib.auth.models import User

@login_required
def chat_view(request, recipient_id):
    """View to display chat messages between the logged-in user and another user."""
    recipient = User.objects.get(id=recipient_id)
    messages = Message.objects.filter(
        (models.Q(sender=request.user) & models.Q(recipient=recipient)) |
        (models.Q(sender=recipient) & models.Q(recipient=request.user))
    ).order_by('timestamp')

    if request.method == "POST":
        content = request.POST.get('message')
        if content:
            Message.objects.create(sender=request.user, recipient=recipient, content=content)
            return redirect('chat_view', recipient_id=recipient.id)

    return render(request, 'chat.html', {'messages': messages, 'recipient': recipient})

@login_required
def users_list(request):
    """View to list all users to start a chat."""
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'users_list.html', {'users': users})


