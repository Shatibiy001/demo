from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name', 'username', 'email', 'short_intro', 'bio',
            'profile_image', 'social_github', 'social_twitter',
            'social_linkedin', 'social_website', 'location'
        ]
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 6}),
            'short_intro': forms.TextInput(attrs={'placeholder': 'e.g. Full-stack developer • React & Python'}),
        }