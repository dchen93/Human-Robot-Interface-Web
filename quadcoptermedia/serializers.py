from .models import User, File
from rest_framework import serializers

class FileSerializer(serializers.ModelSerializer):
	class Meta:
		model = File
		fields = ('user','uploaded_file')
		# user = serializers.Field(source='user.username')