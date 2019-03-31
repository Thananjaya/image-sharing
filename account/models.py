from django.db import models
from django.conf import settings

class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	date_of_birth = models.DateField(null = True, blank = True)
	image = models.ImageField(upload_to= 'users/%y/%m/%d/', blank = True, null = True)

	def __str__(self):
		return 'Profile of {}'.format(self.user.username)
		