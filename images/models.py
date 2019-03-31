from django.db import models
from django.conf import settings
from django.utils.text import slugify

class Image(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'images')
	users_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'images_liked', blank = True)
	title = models.CharField(max_length = 200)
	description = models.TextField(blank =True)
	slug = models.SlugField(max_length = 100)
	url = models.URLField()
	image = models.ImageField(upload_to = 'images/%y/%m/%d')
	created = models.DateField(auto_now_add = True, db_index = True)

	def __str__(self):
		return self.title

