from django import forms 
from .models import WebsiteFormModel

class WebsiteForm(forms.ModelForm):
    class Meta:
        model = WebsiteFormModel
        fields = '__all__'
        labels = {
            'found_what_needed': 'Did u find?'
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-name'
            }),
            'reason_to_visit': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4, 'cols': 40}),
            'first_time_visit': forms.RadioSelect(attrs={
                'class': 'form-control'
            }),
            'found_what_needed': forms.RadioSelect(attrs={
                'class': 'form-control'
            }),
        }
        
