from django.shortcuts import render

# Create your views here.
from .forms import SignUpForm
from videos.models import Video

def home(request):
	# if request.method == "POST":
	# 	# print request.POST
	title = "Welcome to my site"
	form = SignUpForm(request.POST or None)
	videos = Video.objects.all()
	context = {
		"title":title,
		"form":form,
		"videos":videos

	}
	return render(request,"home.html",context)
