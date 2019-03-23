"""
	Using pre defined authenticate middleware from django
	methods:
		authenticate: used to check whether the user credentials and returns the user object
		login: used to initiate the session and login to the web site if the user is valid
"""
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm

@login_required
def dashboard(request):
	"""
		View for successfully redirecting the dashboard after successfull sign-in
	"""
	return render(request, 'account/dashboard.html', {'section': 'dashboard'})

def registration(request):
	"""
		View for registering a new user

		arguements:
			request: an http request method
	"""
	if request.method == 'POST':
		registration_form = RegistrationForm(request.POST)
		if registration_form.is_valid():
			data = registration_form.cleaned_data
			new_user = registration_form.save(commit= False)
			new_user.set_password(data['password'])
			new_user.save()
			return render(request, 'account/registration_successfull.html', {'new_user': new_user, 'cleaned_data': data, 'form': registration_form})
	else:
		registration_form = RegistrationForm()
		return render(request, 'account/registration_form.html', {'form': registration_form})

# to study how django authentication works
# def login(request):
# 	"""
# 		View for user login

# 		arguements:
# 			request: it takes an http request, which should be POST
# 	"""
# 	if request.method == 'POST':
# 		login_form = LoginForm(request.POST)
# 		if login_form.is_valid():
# 			data = login_form.cleaned_data
# 			user = authenticate(request, username = data['username'], password = data['password'])
# 			if user is not None:
# 				if user.is_active:
# 					login(request, user)
# 					return HttpResponse('user successfully signed in')
# 				else:
# 					return HttpResponse('user is disabled')
# 			else:
# 				return HttpResponse('Invalid user')
# 	else:
# 		login_form = LoginForm()
# 	return render(request, 'account/login.html', {'form': login_form})

