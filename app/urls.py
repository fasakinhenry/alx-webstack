from django.urls import path
from . import views

urlpatterns = [
        path('admin/', 
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
]
