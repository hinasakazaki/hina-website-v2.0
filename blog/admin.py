
from django.contrib import admin
from blog.models import Post

class PostAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'post_title', 'post_text']
	list_filter = ['pub_date']
	search_fields = ['post_title']
admin.site.register(Post, PostAdmin)