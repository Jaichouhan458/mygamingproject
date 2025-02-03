from django import forms
from .models import  Data  # Replace with your model name

class ContactForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name', 'lastname', 'email', 'message']
