from django import forms;
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    model = CustomUser
    fields = ('username', 'email', 'department', 'employee_cell_phone')
    
class CustomUserChangeForm(UserChangeForm):
    model = CustomUser
    fields = ('username', 'email', 'department', 'employee_cell_phone')