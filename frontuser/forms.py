from django import forms
from .models import*
from django.contrib.auth.models import User

class userform(forms.ModelForm):
	username = forms.CharField(required=True,max_length=50)
	email = forms.CharField(required=True,max_length=50)
	first_name = forms.CharField(required=True,max_length=50)
	last_name = forms.CharField(required=True,max_length=50)
	password = forms.CharField(required=True,max_length=50)
	confirm_password = forms.CharField(required=True,max_length=50)

	class Meta():
		model=User
		fields=['username','email','first_name','last_name','password']