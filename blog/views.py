from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext, loader

def index(request):
	latest_post = Post.objects.all()[Post.objects.count()-1]
	template = loader.get_template('index.html')
	context = RequestContext(request, {
		'latest_post': latest_post, 'archives' : False,
	})
	return HttpResponse(template.render(context))

def archive(request):
	all_posts = Post.objects.order_by('-pub_date')
	template = loader.get_template('index.html')
	context = RequestContext(request, {
    	'all_posts' : all_posts, 'archives' : True, 
    	})
	return HttpResponse(template.render(context))

def detail(request, post_id):
	try:
		post = Post.objects.get(pk=post_id)
	except Post.DoesNotExist:
		raise Http404("Post does not exist")
	template = loader.get_template('index.html')
	context = RequestContext(request, {
		'latest_post': post, 'archives' : False,
	})
	return HttpResponse(template.render(context))