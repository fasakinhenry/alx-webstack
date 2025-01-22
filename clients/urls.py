from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='client_home'),
    path('register/', views.register, name='client_register'),
    path('login/', views.register, name='client_login'),
    path('dashboard/', views.dashboard, name='client_dashboard'),
    path('edit-profile/', views.edit_profile, name='client_edit_profile'),
    path('logout/', views.client_logout, name='client_logout'),
    path('employees/', views.employees, name='client_employees'),
    path('profile/', views.profile_view, name='client_profile_view'),
    # Add other URL patterns here


    #chat
    path('chat/<int:recipient_id>/', views.chat_view, name='chat_view'),
    path('users/', views.users_list, name='users_list'),
]
