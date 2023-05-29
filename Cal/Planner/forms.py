from django import forms

from .models import Item, User

class NewItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields='__all__'

class NewUserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields='__all__'