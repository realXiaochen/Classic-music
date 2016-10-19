from django.shortcuts import render
from .forms import SignUpForm
import random
from videos.models import Video



# Create your views here.

def home(request):
	# if request.method == "POST":
	# 	# print request.POST
	title = "Welcome to my site"
	form = SignUpForm(request.POST or None)

	random_idx = random.randint(0, Video.objects.count() - 1)
	random_video = Video.objects.all()[random_idx]
	random_videos = Video.objects.all().order_by('?')[:8]
	context = {
		"title":title,
		"form":form,
		"random_video":random_video,
		"random_videos":random_videos,
	}
	return render(request,"home.html",context)
