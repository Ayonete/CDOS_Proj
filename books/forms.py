"""
Defines the forms used for the book application. The form is used in views.py to handle user input
"""

from django.forms import ModelForm
from django import forms
from .models import Book


# declaring the ModelForm
# pylint: disable=too-few-public-methods
class EditBookForm(ModelForm):
    """ this class defines fields for the book model"""
    class Meta:
        # the Model from which the form will inherit from
        model = Book
        # the fields we want from the Model
        fields = ['title', 'author', 'review','rating', 'image']
        # styling the form with bootstrap classes
        widgets = {
             'title': forms.TextInput(attrs={'class': 'form-control'}),
             'author': forms.TextInput(attrs={'class': 'form-control'}),
             'review': forms.Textarea(attrs={'class': 'form-control'}),
             'rating': forms.Textarea(attrs={'class': 'form-control'})
             #'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
