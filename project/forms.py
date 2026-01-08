from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'owner', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Project Title'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Describe your project...',
                'rows': 5
            }),
            'demo_link': forms.URLInput(attrs={
                'class': 'form-input',
                'placeholder': 'Demo Link'
            }),
            'source_link': forms.URLInput(attrs={
                'class': 'form-input',
                'placeholder': 'Source Code Link'
            }),
            'tags': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Comma-separated tags'
            }),
        }
