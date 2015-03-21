from django.shortcuts import render
from comix.models import ComicPost
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext, loader

def comix(request):
	latest_post = ComicPost.objects.all()[ComicPost.objects.count()-1]
	template = loader.get_template('comix.html')
	context = RequestContext(request, {
		'latest_post': latest_post, 'archives' : False,
	})
	return HttpResponse(template.render(context))

def archive(request):
	all_posts = ComicPost.objects.order_by('-pub_date')
	template = loader.get_template('comix.html')
	context = RequestContext(request, {
    	'all_posts' : all_posts, 'archives' : True, 
    	})
	return HttpResponse(template.render(context))

def detail(request, post_id):
	try:
		post = ComicPost.objects.get(pk=post_id)
	except ComicPost.DoesNotExist:
		raise Http404("ComicPost does not exist")
	template = loader.get_template('comix.html')
	context = RequestContext(request, {
		'latest_post': post, 'archives' : False,
	})
	return HttpResponse(template.render(context))