from django.conf.urls import url, patterns
from django.contrib import admin
from polls import views

urlpatterns =['',
    url(r'^polls/$', views.index, name='index'),
    url(r'^polls/(?P<question_id>\d+)/$', views.detail, name='detail'),
    url(r'^polls/(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^polls/(?P<question_id>\d+)/results/$', views.results, name='results'),
]
