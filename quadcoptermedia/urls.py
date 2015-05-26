from django.conf.urls import patterns, url
from quadcoptermedia import views

urlpatterns = patterns('',
	#url(r'^$', views.DetailView.as_view(), name='detail'),
	url(r'^$', views.index, name='index'),
	url(r'^user/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	# url(r'^media/(?P<pk>\d+)/$', views.MediaView.as_view(), name='uploaded_media'),
)