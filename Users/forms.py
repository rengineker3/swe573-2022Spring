from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django.utils import timezone
from django.core.exceptions import ValidationError



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

def validate_date(date):
    if date < timezone.now():
        raise ValidationError("Date cannot be in the past.")

def validate_date_after(date):
    if date > timezone.now():
        raise ValidationError("Date cannot be in the future.")

class DateTimeLocalInput(forms.DateTimeInput):
    input_type = "datetime-local"
 
class DateTimeLocalField(forms.DateTimeField):
    input_formats = [
        "%Y-%m-%dT%H:%M:%S", 
        "%Y-%m-%dT%H:%M:%S.%f", 
        "%Y-%m-%dT%H:%M"
    ]
    widget = DateTimeLocalInput(format="%Y-%m-%dT%H:%M")


class UserUpdateForm(forms.ModelForm):
    
    email = forms.EmailField()
    label = 'E-mail'
    
    name = forms.CharField(
        label = 'Name',
        widget = forms.Textarea(attrs={
            'rows': '1',
            'placeholder': 'Your name...'
        })
    )
    
    bio = forms.CharField(
        label = 'Bio',
        widget = forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Your bio...'
        })
    )

    occupation = forms.CharField(
        label = 'Occupation',
        widget = forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Your job...'
        })
    )


    class Meta:
        model = User
        fields = ['email', 'name', 'bio', 'occupation']
    


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

        
