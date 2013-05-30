from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from qanda.models import Department, Course, Professor, Question, Answer

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('qanda.views',
	url(r'^$', 'index'),
	url(r'^(?P<department_id>\d+)/$', 'courses'),
	url(r'^(?P<department_id>\d+)/(?P<course_id>\d+)/$', 'professors'),
	url(r'^(?P<department_id>\d+)/(?P<course_id>\d+)/(?P<professor_id>\d+)/$', 'questions'),
	url(r'^(?P<department_id>\d+)/(?P<course_id>\d+)/(?P<professor_id>\d+)/(?P<question_id>\d+)/$', 'answers'),
)