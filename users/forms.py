from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	first_name = forms.CharField(max_length=20, label='First Name')
	last_name = forms.CharField(required=False, max_length=20, label='Last Name (optional)')
	email = forms.EmailField()
	
	# Meta is used to change the behavior/structure of model fields like changing order options,verbose_name and more in forms.
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username','email','password1','password2']

class UserUpdateForm(forms.ModelForm): #ModelForm is a form that allows to create form that will work with specific database model
	first_name = forms.CharField(max_length=20, label='First Name')
	last_name = forms.CharField(required=False, max_length=20, label='Last Name (optional)')
	email = forms.EmailField()
	
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'username','email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']
		labels = {'image':'Profile Image'}