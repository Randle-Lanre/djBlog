from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#import profile since we would be working with it
from .models import Profile


class UserRegisterForm(UserCreationForm):
	email=forms.EmailField()

	class Meta:
		model=User
		fields=['username', 'email', 'password1', 'password2']

#allows username and email to be updated
class UserUpdateForm(forms.ModelForm):
	email= forms.EmailField()

	class Meta:
		model=User
		fields=['username','email']

#allows user profile image to be updated
class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=['image']

#then add to the views