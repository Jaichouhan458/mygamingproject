from django import forms
from .models import  Data,User_Info  # Replace with your model name

class ContactForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['name', 'lastname', 'email', 'message']



class UserSignUp(forms.ModelForm):
    class Meta:
        model =  User_Info
        fields =  ["fullname","username","email","Password"]