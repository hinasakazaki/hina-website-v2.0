from django.db import models
from tinymce.models import HTMLField

class Post(models.Model):
	post_title = models.CharField(max_length=60)
	post_text = HTMLField()
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.post_title