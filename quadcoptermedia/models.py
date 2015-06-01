from django.db import models

from django.utils import timezone

# Create your models here.


class User(models.Model):
	username = models.CharField(max_length=200)
	active = models.BooleanField(default=False) # for synchronizing with google glass

	def __str__(self):
		return self.username


class File(models.Model):
	user = models.ForeignKey(User)
	uploaded_file = models.FileField(upload_to='%Y/%m/%d')
	# uploaded_thumbnail = models.FileField(upload_to = '%Y/%m/%d')
	class Meta:
		ordering = ['-id']

	def __str__(self):
		return self.uploaded_file.name

