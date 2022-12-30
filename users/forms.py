from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# inherits from the UserCreationForm


class UserRegisterForm(UserCreationForm):
    # adds email field to the form
    email = forms.EmailField()

    class Meta:
        model = User  # model that will be affected
        fields = ['username', 'email', 'password1', 'password2']
# we can use this form in the template instead of the UserCreationForm
# allows us to update the user's profile


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User  # model that will be affected
        # we only want to update the email field and username field
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        # model we want to update is the Profile model
        model = Profile
        # we only want to update the image field
        fields = ['image']
