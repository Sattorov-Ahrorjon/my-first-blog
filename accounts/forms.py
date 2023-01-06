from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


# Malumot kiritish uchun class
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age')


# Malumotlarni tahrirlash uchun class
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'age')
