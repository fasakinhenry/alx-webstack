from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='clients_home'),
    path('register/', views.register, name='clients_register'),
    path('login/', views.register, name='clients_login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('logout/', views.logout_view, name='logout'),
    path('view-users/', views.view_users, name='view_users'),
    path('profile/', views.profile_view, name='profile_view'),
    # Add other URL patterns here
]