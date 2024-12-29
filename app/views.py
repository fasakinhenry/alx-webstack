from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from .forms import ClientForm
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def base(request):      
    form = ClientForm()
    """if request.method == 'POST':                
        form = ClientForm(request.POST, request.FILES)                                          
        if form.is_valid():         
            form.save()             
            return redirect('client_list')  # Redirect to the list view after success           
        else:                   
            form = ClientForm()"""
    return render(request, 'app/bass.html', {'form':form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate user
            user = form.get_user()
            login(request, user)
            messages.success(request, "You have successfully logged in.")
            return redirect('home')  # Redirect to a home page or dashboard
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'app/login.html', {'form': form})


@login_required
def home(request):
    return render(request, 'home.html')


#logout
def logout_view(request):
    logout(request)
    return redirect('login')


# Register a new Client
def register_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('client_list')  # Redirect to the list view after success
    else:
        form = ClientForm()
    return render(request, 'app/register_client.html', {'form': form})


# List all clients
def client_list(request):
    client = Client.objects.all()
    return render(request, 'app/client_list.html', {'client': client})

# View details of a single client
def client_detail(request, pk):
    client = get_object_or_404(client, pk=pk)
    return render(request, 'app/customer_detail.html', {'client': client})


# Edit a client  details
def client_edit(request, pk):
    client = get_object_or_404(client, pk=pk)
    if request.method == 'POST':
        form = clientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_detail', pk=pk)
    else:
        form = ClientForm(instance=client)
    return render(request, 'app/client_form.html', {'form': form})



# Delete a service provider
def client_delete(request, pk):

    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'app/client_confirm_delete.html', {'client': client})

   


#API

# from rest_framework.views import APIView
#from rest_framework.response import Response
#from rest_framework import status
#from .models import Client
#from .serializers import ClientSerializer
"""
class RegisterClientAPI(APIView):
    def post(self, request, format=None):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




        """
