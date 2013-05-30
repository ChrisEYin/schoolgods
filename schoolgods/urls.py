from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', include('qanda.urls')),
	url(r'^home/', include('qanda.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
