from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserSignupForm


class SignUpView(CreateView):
    form_class = CustomUserSignupForm
    success_url = reverse_lazy("ponderings:pondering-index")
    template_name = "registration/signup.html"