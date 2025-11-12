from django.contrib.auth.forms import AdminUserCreationForm, UserChangeForm, UserCreationForm
from .models import CustomUser

class CustomUserSignupForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email", "username", "first_name", "last_name",)


class CustomUserCreationForm(AdminUserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email", "username", "first_name", "last_name",)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email", "username", "first_name", "last_name",)