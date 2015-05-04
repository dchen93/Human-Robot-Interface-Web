from quadcoptermedia.models import UploadGroup, File
from django.forms import widgets
from rest_framework import serializers

class FileSerializer(serializers.ModelSerializer):
	class Meta:
		model = File
		fields = ('date', 'uploaded_file')

