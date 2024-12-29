from django.contrib import admin
from django.contrib import admin
from .models import Client


@admin.register(Client)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'gender', 'location')

# Register your models here.


