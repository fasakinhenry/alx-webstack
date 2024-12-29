from django.urls import path
from . import views
#from .views import RegisterClientAPI
urlpatterns = [
    #URL for base
    path('', views.base, name='base'),

    # URL for registering a client
    path('register/', views.register_client, name='register_client'),

    # URL for listing client
    path('list/', views.client_list, name='client_list'),

    # URL for viewing a client details
    path('detail/<int:pk>/', views.client_detail, name='client_detail'),

    # URL for editing a client
    path('edit/<int:pk>/', views.client_edit, name='client_edit'),

    # URL for deleting a client
    path('delete/<int:pk>/', views.client_delete, name='client_delete'),
    #URL for client login
    path('login/', views.login_view, name='login'),

    # URL for logout
    path('logout/', views.logout_view, name='logout'),


    #API

#    path('api/register-client/', RegisterClientAPI.as_view(), name='register_client_api'),
            ]
