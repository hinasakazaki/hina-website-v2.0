from django.shortcuts import render
from projects.models import Project
from django.http import HttpResponse
from django.http import Http404
from django.template import RequestContext, loader

def projects(request):
	all_posts = Project.objects.order_by('-pub_date')
	template = loader.get_template('projects.html')
	context = RequestContext(request, {
    	'all_posts' : all_posts, 'archives' : True, 
    	})
	return HttpResponse(template.render(context))

# return HttpResponse(template.render(context))
# 	latest_post = Project.objects.all()[Project.objects.count()-1]
# 	template = loader.get_template('projects.html')
# 	context = RequestContext(request, {
# 		'latest_post': latest_post, 'archives' : False,
# 	})
# def archive(request):
# 	all_posts = ComicPost.objects.order_by('-pub_date')
# 	template = loader.get_template('comix.html')
# 	context = RequestContext(request, {
#     	'all_posts' : all_posts, 'archives' : True, 
#     	})
# 	return HttpResponse(template.render(context))

# def detail(request, post_id):
# 	try:
# 		post = ComicPost.objects.get(pk=post_id)
# 	except ComicPost.DoesNotExist:
# 		raise Http404("ComicPost does not exist")
# 	template = loader.get_template('comix.html')
# 	context = RequestContext(request, {
# 		'latest_post': post, 'archives' : False,
# 	})
# 	return HttpResponse(template.render(context))