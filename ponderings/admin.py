from django import forms
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.auth.forms import AuthenticationForm

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class UsernameOrEmailAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="Email or Username",
        widget=forms.TextInput(attrs={'autofocus': True})
    )

class CustomAdminSite(AdminSite):
    login_form = UsernameOrEmailAuthenticationForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    ]
    list_filter = ("email", "username", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "username", "first_name", "last_name", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "username", "first_name", "last_name", "password1", "password2",
                "is_staff", "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email", "username", "first_name", "last_name",)
    ordering = ("email",)

admin_site = CustomAdminSite(name='customadmin')
admin_site.register(Group, GroupAdmin)
admin_site.register(CustomUser, CustomUserAdmin)