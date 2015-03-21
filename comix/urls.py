from django.conf.urls import patterns, url

from comix import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.comix, name='comix'),
    url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
    url(r'^archive/', views.archive, name='archive'),
    )