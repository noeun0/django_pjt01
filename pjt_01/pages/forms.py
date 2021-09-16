from .models import Page
from django import forms

class PagesForm(forms.ModelForm):
    class Meta():
        model = Page
        fields = '__all__'
