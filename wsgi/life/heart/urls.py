from django.conf.urls import patterns, include, url
from heart import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^index$', views.index, name='index'),
	url(r'^do$', views.do, name='do'),
	url(r'^reset$', views.reset, name='reset'),
	)
