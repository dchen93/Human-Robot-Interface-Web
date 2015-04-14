from django.db import models

from django.utils import timezone

# Create your models here.


class UploadGroup(models.Model):
	upload_group = models.DateField('Date Uploaded', default=timezone.now)

	def __str__(self):
		return self.upload_group.strftime('%b %d, %Y')


class File(models.Model):
	date = models.ForeignKey(UploadGroup)
	uploaded_file = models.FileField(upload_to='%Y/%m/%d')
	# uploaded_thumbnail = models.FileField(upload_to = '%Y/%m/%d')

	def __str__(self):
		return self.uploaded_file.name