from django.conf.urls import patterns, url
from apps.board import views
urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^process/$', views.process_point, name='process')
)