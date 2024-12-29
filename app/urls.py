from django.urls import path
from . import views
from .views import ClientListView, ClientDetailView, UserCreateView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('api/users/', UserCreateView.as_view(), name='user-create'),
    path('api/clients/', ClientListView.as_view(), name='client-list'),
    

    path('clients/', ClientListView.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),


    path('api-token-auth/', obtain_auth_token),
    
    path("", views.base, name='base'),



    ]


