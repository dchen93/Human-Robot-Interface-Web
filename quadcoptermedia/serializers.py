from .models import UploadGroup, File
from rest_framework import serializers

class FileSerializer(serializers.ModelSerializer):
	class Meta:
		model = File
		fields = ('date','uploaded_data')