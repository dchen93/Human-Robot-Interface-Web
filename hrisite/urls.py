from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from quadcoptermedia import views

# router = routers.DefaultRouter()
# router.register(r'files', views.FileUpload)

urlpatterns = [
    # Examples:
    url(r'^$', 'hrisite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^quadcoptermedia/', include('quadcoptermedia.urls', namespace='quadcoptermedia')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/upload/$', views.FileUpload.as_view(), name='file_set'),
    url(r'^api/upload/(?P<pk>[0-9]+)/$', views.FileDetail.as_view(), name='file_detail'),
    url(r'^api/active/$', views.ActiveUser.as_view(), name='active_user'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }, name='media'),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
        }),
)