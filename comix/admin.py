
from django.contrib import admin
from comix.models import ComicPost

class ComicPostAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'post_title', 'image', 'post_text']
	list_filter = ['pub_date']
	search_fields = ['post_title']
admin.site.register(ComicPost, ComicPostAdmin)