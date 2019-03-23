from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget= forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
	password = forms.CharField(label="password", widget= forms.PasswordInput)
	password2 = forms.CharField(label="confirm password", widget= forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email']

	def clean_password2(self):
		data = self.cleaned_data
		if data['password'] != data['password2']:
			raise form.ValidationError('Password doesn\'t match')
		return data['password2']
