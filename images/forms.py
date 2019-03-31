from django import forms
from .models import Image

class ImageCreationForm(forms.ModelForm):

	class Meta:
		model = Image
		fields = ('title', 'description', 'url')
		widgets = {
			'url': forms.HiddenInput
		}

		def clean_url(self):
			"""
				checking whether the incomming url has the valid extensions
				this method will be called when the is_valid() function is called in the view part 
			"""
			url = self.cleaned_data['url']
			valid_extensions = ['jpg', 'jpeg']
			extension = url.rsplit('.', 1)[1].lower()
			if extension not in valid_extensions:
				raise forms.ValidationError('the given image is not with the valid extensions')
			return url
