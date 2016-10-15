from django.contrib import admin

# Register your models here.

from .models import Video
from .forms import VideoForm

class VideoAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","created"]
	form = VideoForm

admin.site.register(Video,VideoAdmin)