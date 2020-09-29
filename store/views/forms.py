from django.core import validators
from django import forms
from store.models.product import Product
from store.models.category import Category


class DetailsForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','category','image','description']
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'category' : forms.TextInput(attrs={'class':'form-control'}),
            'image' : forms.FileInput(attrs={'class': 'form-control'}),
            'description' : forms.TextInput(attrs={'class':'form-control'}),
        }

