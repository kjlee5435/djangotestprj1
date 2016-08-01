from django.conf.urls import url, include
from django.contrib import admin
from sensorLoggingApi import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'submit/$', views.submit, name='submit'),
    url(r'postfile/$', views.postfile, name='postfile'),

#    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
#    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
 ]
