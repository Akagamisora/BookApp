from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publish_date', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'mt-1 block w-full shadow-sm border-gray-300 rounded-md'}),
            'author': forms.TextInput(attrs={'class': 'mt-1 block w-full shadow-sm border-gray-300 rounded-md'}),
            'publish_date': forms.DateInput(attrs={'class': 'mt-1 block w-full shadow-sm border-gray-300 rounded-md', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'mt-1 block w-full shadow-sm border-gray-300 rounded-md'}),
        }