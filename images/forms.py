from django import forms
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify  
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

		def save(self, force_insert=False, force_update=False, commit=True):
			"""
				Overriding the save method,
				this method will be called whenever the save() method is called in the view part
			"""
			image = super(ImageCreationForm, self).save(commit= False)
			url = self.cleaned_data['url']
			description = self.cleaned_data['description']
			name = '{}.{}'.format(slugify(self.title), url.rsplit('.', 1)[1].lower())
			image_file = request.urlopen(url)
			# image.image.save(name, ContentFile(image_file.read()) , save=False)
			if commit:
				image.save(name, description, ContentFile(image_file.read()))
			return image
