from django.conf.urls import patterns, url
from quadcoptermedia import views

urlpatterns = patterns('',
	#url(r'^$', views.DetailView.as_view(), name='detail'),
	url(r'^$', views.index, name='index'),
	url(r'^user/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
	url(r'^pair/$', views.pair, name='pair'),
	url(r'^pending/$', views.PendingView.as_view(), name='pending'),
	url(r'^update/$', views.update, name='update'),
	# url(r'^media/(?P<pk>\d+)/$', views.MediaView.as_view(), name='uploaded_media'),
)