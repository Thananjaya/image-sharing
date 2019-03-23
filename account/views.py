"""
	Using pre defined authenticate middleware from django
	methods:
		authenticate: used to check whether the user credentials and returns the user object
		login: used to initiate the session and login to the web site if the user is valid
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login(request):
	"""
		View for user login

		arguements:
			request: it takes an http request, which should be POST
	"""
	if request.method == 'POST':
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			data = login_form.cleaned_data
			user = authenticate(request, username = data['username'], password = data['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponse('user successfully signed in')
				else:
					return HttpResponse('user is disabled')
			else:
				return HttpResponse('Invalid user')
	else:
		login_form = LoginForm()
	return render(request, 'account/login.html', {'form': login_form})