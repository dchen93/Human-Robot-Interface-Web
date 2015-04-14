from django.contrib import admin

from quadcoptermedia.models import UploadGroup, File

# Register your models here.

class FileInLine(admin.StackedInline):
	model = File
	extra = 3

class UploadGroupAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,		{'fields': ['upload_group']}),
	]
	inlines = [FileInLine]
	list_filter = ['upload_group'] #date
	search_fields = ['upload_group']

admin.site.register(UploadGroup, UploadGroupAdmin)