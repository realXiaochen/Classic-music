from django.contrib import admin

# Register your models here.

from .models import Video, Category, VideoImage, CategoryImage
from .forms import VideoForm, CategoryForm

class VideoAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","created"]
	form = VideoForm

admin.site.register(Video,VideoAdmin)

class CategoryAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","created",]
	form = CategoryForm


admin.site.register(Category,CategoryAdmin)

admin.site.register(VideoImage)
admin.site.register(CategoryImage)