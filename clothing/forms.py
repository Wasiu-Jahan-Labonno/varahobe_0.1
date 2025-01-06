
from django import forms
from .models import Clothing

from django import forms
from .models import Clothing


class ClothingForm(forms.ModelForm):
    class Meta:
        model = Clothing
        fields = ['title', 'description', 'area', 'address', 'price', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title of the house'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Provide a detailed description',
                'style': 'height: 200px;'
            }),
            'area': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the area of the house'
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the address of the house'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the price of the house'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }
