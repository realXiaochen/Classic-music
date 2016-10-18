from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import random
# Create your views here.

from .models import Video, Category

class VideoDetailView(DetailView):
	model = Video
	def get_context_data(self,*args,**kwargs):
		context = super(VideoDetailView, self).get_context_data(*args, **kwargs)
		instance = self.get_object()
		context["related"] = sorted(Video.objects.get_related(instance), key=lambda x:random.random())
		return context


class VideoListView(ListView):
	model = Video
	def get_context_data(self, **kwargs):
		context = super(VideoListView, self).get_context_data(**kwargs)
		context['number'] = 1
		return context
	def get_queryset(self,*args,**kwargs):
		qs = super(VideoListView,self).get_queryset(*args,**kwargs)
		query = self.request.GET.get("q")
		if query:
			qs = self.model.objects.filter(
				Q(title__icontains=query) |
				Q(description__icontains=query)
				)
		return qs




class CategoryListView(ListView):
	model = Category
	queryset = Category.objects.all()

class CategoryDetailView(DetailView):
	model = Category





# def video_detail_view_func(request, id):
# 	video_instance = Video.objects.get(id=id)
# 	template = "videos/video_detail.html"
# 	context = {
# 		"object": video_instance
# 	}
# 	return render(request, template, context)

