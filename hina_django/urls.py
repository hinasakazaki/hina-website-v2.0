from django.conf.urls import patterns, include, url
from django.contrib import admin
from hina_django import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hina_django.views.home', name='home'),
    url(r'^index/', include('blog.urls')),
    url(r'^comix/', include('comix.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^contact/', views.contact),
    url(r'^fotos/', views.fotos),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    # url(r'^index/', include('index.urls')),
    # url(r'^blog/', include('blogposts.urls')),
    # url(r'^comix/', include ('comix.urls')),
    # url(r'^projects/', include ('projects.urls')),
    # url(r'^contact/', include ('contact.urls')),
    )