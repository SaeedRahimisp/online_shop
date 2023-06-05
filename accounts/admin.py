from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangForm, CustomUserCreationForm
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    form = CustomUserChangForm
    list_display = ('email', 'username', )