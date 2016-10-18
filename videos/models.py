
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.
class VideoQuerySet(models.query.QuerySet):
	def active(self):
		return self.filter(active=True)

class VideoManager(models.Manager):
	def get_queryset(self):
		return VideoQuerySet(self.model, using = self._db)

	def all(self, *args, **kwargs):
		return self.get_queryset().active()

	def get_related(self, instance):
		products_one = self.get_queryset().filter(categories__in=instance.categories.all())
		# products_two = self.get_queryset().filter(default = instance.default)
		qs = products_one.exclude(pk=instance.pk).distinct()
		return qs




class Video(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField(blank = True,null=True)
	video_url = models.CharField(max_length=120)
	picture_url = models.CharField(max_length=120)
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True,auto_now=False)
	categories = models.ManyToManyField('Category')
	default = models.ForeignKey('Category', related_name='default_category',null = True, blank = True)	


	objects = VideoManager()

	class Meta:
		ordering = ["title"]

	def __unicode__(self):
		return str(self.title)

	def get_absolute_url(self):
		return reverse("video_detail", kwargs={"pk":self.pk})


class Category(models.Model):
	title = models.CharField(max_length=120, unique = True)
	slug = models.SlugField(unique=True)
	description = models.TextField(null=True, blank=True)
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("category_detail", kwargs={"slug":self.slug})

	def get_video_list(self):
		return Video.objects.all.filter()

class VideoImage(models.Model):
	video = models.ForeignKey(Video)
	image = models.ImageField(upload_to="img/video_img")

	def __unicode__(self):
		return self.video.title

class CategoryImage(models.Model):
	category = models.ForeignKey(Category)
	image = models.ImageField(upload_to="img/category_img")

	def __unicode__(self):
		return self.category.title




















