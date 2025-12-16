from django.shortcuts import render
from ponderings.models import Pondering

def home(request):
    if request.user.is_authenticated:
        ponderings = Pondering.objects.filter(user=request.user).order_by("-created_at")
    else:
        ponderings = Pondering.objects.filter(private=False).order_by("-created_at")

    return render(request, 'home.html', {'ponderings': ponderings})