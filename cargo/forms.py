from django.forms import ModelForm
from django import forms
from .models import Cargo

class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'