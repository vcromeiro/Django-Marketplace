from django import forms
from home.models import Product


class HomeForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a Name...',
        }    
    ))
    image = forms.ImageField(required=False)
    description = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a Description...',
        }     
    ))
    price = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Set a Price...',
            'type': 'number',
        }     
    ))
    class Meta:
        model = Product
        fields = (
            'name',
            'image',
            'description',
            'price',
        
        )
        
        