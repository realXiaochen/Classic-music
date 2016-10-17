"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
# from videos.views import video_detail_view_func

from .views import VideoDetailView, VideoListView


# from newsletter import views as newsletter_views
# from videos import urls as videos_url



urlpatterns = [

    url(r'^$',VideoListView.as_view(), name = "video_list"),
    url(r'^(?P<pk>\d+)', VideoDetailView.as_view(), name = "video_detail"),
]
