from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from .forms import ClientForm


# Register a new Client
def register_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('client_list')  # Redirect to the list view after success
    else:
        form = ClientForm()
    return render(request, 'register_client.html', {'form': form})


# List all clients
def client_list(request):
    client = Client.objects.all()
    return render(request, 'client_list.html', {'client': client})

# View details of a single client
def client_detail(request, pk):
    client = get_object_or_404(client, pk=pk)
    return render(request, 'customer_detail.html', {'client': client})


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
    return render(request, 'client_form.html', {'form': form})


# Delete a service provider
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'client_confirm_delete.html', {'client': client})
    
