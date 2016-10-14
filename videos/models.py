from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Video(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(blan = True,null=True)
	video_url = models.CharField(max_length=120)
	picture_url = models.CharField(max_length=120)
	#slug


	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True,auto_now=False)
	category

	def __unicode__(self):
		return self.title