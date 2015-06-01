from django.contrib import admin

from quadcoptermedia.models import User, File

# Register your models here.

class FileInLine(admin.StackedInline):
	model = File
	extra = 3

class UserAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,					{'fields': ['username']}),
		# ('Ready to Connect',	{'fields': ['active']}),
	]
	inlines = [FileInLine]
	list_display = ('username','active')
	search_fields = ['username']

admin.site.register(User, UserAdmin)