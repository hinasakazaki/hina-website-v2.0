from django.contrib import admin
from projects.models import Project

class ProjectAdmin(admin.ModelAdmin):
	fields = ['project_title', 'project_link', 'image', 
	'project_text', 'pub_date']
	list_filter = ['pub_date']
	search_fields = ['project_title']
admin.site.register(Project, ProjectAdmin)