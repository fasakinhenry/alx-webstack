# filepath: /home/tobijah/alx/alx-webstack/serviceproviders/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('editprofile/', views.edit_profile, name='edit_profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile_view, name='profile_view'),
    path('view-users/', views.view_users, name='view_users'),
    path('about/', views.about, name='about'),
    path('jobs/', views.jobs, name='jobs'),
    path('freelancer/', views.freelancer, name='freelancer'),
    path('employees/', views.employees, name='employees'),
    path('tables/', views.tables, name='tables'),
    path('api/profiles/', views.profiles_api, name='profiles_api'),  # Use profiles_api view
]