from pyexpat import model
from django import forms
from .models import aman
class mahajan(forms.ModelForm):
    class Meta:
        model=aman
        fields="__all__"