import email
from tkinter import Widget
from django import forms
from .models import Select
from django.forms import ModelForm
from .models import Address

class AddressForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Address
        fields = "__all__"
        widgets = {
           'address': forms.TextInput(attrs={'class': 'form-control-lg mb-2'}),
           'state': forms.TextInput(attrs={'class': 'form-control-lg mb-2'}),
           'country': forms.TextInput(attrs={'class': 'form-control-lg mb-2'}),
           'postalcode': forms.TextInput(attrs={'class': 'form-control-lg mb-2'}),

        }
        
class SignupForm(forms.Form):
    username = forms.CharField(max_length=50, label='Username')
    password = forms.CharField(max_length=20)
    confirmpassword = forms.CharField(max_length=20)
    email = forms.EmailField(required=False, label='Your email address')
    
    widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control'}),
        
    }    

class SelectForm(ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Select
        fields ="__all__"
        widgets = {
           'item': forms.TextInput(attrs={'class': 'form-control-lg mb-2'}),
           'quantity': forms.TextInput(attrs={'class': 'form-control-lg mb-2'}),
           'price': forms.TextInput(attrs={'class': 'form-control-lg mb-2'}),
        }
        



