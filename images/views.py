from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreationForm

@login_required
def image_create(request):
	if request.method == 'POST':
		image_creation_form = ImageCreationForm(request.POST)
		if image_creation_form.is_valid():
			data = self.cleaned_data
			new_image = data.save(commit=False)
			new_image.user = request.user
			new_image.save()
			messages.success(request, 'image is been saved successfully')
			return redirect(new_image.get_absolute_url())
	else:
		image_creation_form = ImageCreationForm(request.GET)
	return render(request, 'images/new.html', {'form': image_creation_form, 'section': 'images'})