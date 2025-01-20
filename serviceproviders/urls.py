# filepath: /home/tobijah/alx/alx-webstack/serviceproviders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile_view'),
    path('view-users/', views.view_users, name='view_users'),
    path('api/profiles/', views.profiles_api, name='profiles_api'),  # Use profiles_api view
]