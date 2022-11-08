from django import forms
from django import forms
from .models import Product

class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('user', 'created', 'updated', 'slug')