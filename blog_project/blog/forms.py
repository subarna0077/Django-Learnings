from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'rating', 'slug', 'author']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control', 'rows':5
            }),
             'rating': forms.NumberInput(attrs={
                 'class': 'form-control'
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }

        error_messages= {
            'title': {
                 'required': 'Please enter the blog title',
                'max_length': 'Title should not be greater than 80 words'
            },

            'description': {
                 'required': 'Please enter the blog description',
                'max_length': 'Title should not be greater than 400 words'
            },
            'rating': {
                'required': 'Please enter a rating',
                'min_value': 'Minimum rating is 1',
                'max_value': 'Maximum rating is 5',
            },
             'slug': {
                'required': 'Slug is required',
                'unique': 'This slug is already in use',
            },
             'author': {
                'required': 'Author name is required',
            },
        }
