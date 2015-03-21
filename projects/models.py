from django.db import models
from tinymce.models import HTMLField

class Project(models.Model):
	project_title = models.CharField(max_length=60)
	project_link = models.CharField(max_length=60)
	image = models.ImageField(upload_to = 'static/img/projects')
	project_text = HTMLField()
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.project_title