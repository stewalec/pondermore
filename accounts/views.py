from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserSignupForm


class SignUpView(CreateView):
    form_class = CustomUserSignupForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"