from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render

# Create your views here.

from .models import Video

class VideoDetailView(DetailView):
	model = Video


# def video_detail_view_func(request, id):
# 	video_instance = Video.objects.get(id=id)
# 	template = "videos/video_detail.html"
# 	context = {
# 		"object": video_instance
# 	}
# 	return render(request, template, context)

