from django.shortcuts import render

# Create your views here.
from .forms import SignUpForm

def home(request):
	# if request.method == "POST":
	# 	# print request.POST
	title = "Welcome to my site"
	form = SignUpForm(request.POST or None)
	context = {
		"title":title,
		"form":form,

	}
	return render(request,"home.html",context)
