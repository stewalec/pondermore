from django import forms
from .models import Pondering

class PonderingForm(forms.ModelForm):
    class Meta:
        model = Pondering
        fields = ['content', 'author', 'reference', 'private']