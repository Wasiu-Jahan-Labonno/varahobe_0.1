# houses/forms.py
from django import forms
from .models import House

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['title', 'description', 'area', 'address', 'price', 'image']
