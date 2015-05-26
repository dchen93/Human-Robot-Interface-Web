from django.contrib import admin

from quadcoptermedia.models import User, File

# Register your models here.

class FileInLine(admin.StackedInline):
	model = File
	extra = 3

class UserAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,		{'fields': ['username']}),
	]
	inlines = [FileInLine]
	search_fields = ['username']

admin.site.register(User, UserAdmin)