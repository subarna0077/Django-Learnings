from django import forms
from .models import Review
    
# class ReviewForm(forms.Form):
#     username = forms.CharField(label="Your name", max_length=100, required=True, error_messages= {
#         'required': 'Please enter your name',
#         'max_length': 'Name must be under 50 characters',
        
#     },
#     widget=forms.TextInput(attrs={
#         'class': 'username'
#     })
#     )
#     email = forms.EmailField(help_text="Enter a valid email",  error_messages={
#             'required': 'Email is mandatory.',
#             'invalid': 'Enter a valid email.'
#         },
#         widget=forms.EmailInput(attrs={
#             'class': 'email'
#         })
#     )
#     age = forms.IntegerField(min_value=18, max_value=99,  error_messages={
#             'invalid': 'Age must be a number.',
#             'required': 'Age is required.'
#         }
#     )
#     review = forms.CharField(widget=forms.Textarea(attrs={
#         'class': 'review-texts',
#         'placeholder': 'Enter the review'
#     }))
#     accept_terms = forms.BooleanField(error_messages={
#             'required': 'You must accept the terms.'
#         })


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            'username': 'Your name',
        }
        error_messages= {
            'username': {
                'required': 'Please enter your name',
                'max_length': 'Name must be under 50 characters',
            }    
        }
        
        