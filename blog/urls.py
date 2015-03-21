from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
    url(r'^archive/', views.archive, name='archive'),
    )