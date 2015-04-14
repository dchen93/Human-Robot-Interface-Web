from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'hrisite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^quadcoptermedia/', include('quadcoptermedia.urls', namespace='quadcoptermedia')),
    url(r'^admin/', include(admin.site.urls)),
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