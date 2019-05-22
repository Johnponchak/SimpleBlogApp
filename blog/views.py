from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

def PostList(response):
	bg=Post.objects.all()
	if response.user_agent.is_mobile == True:
		return render(response, "blog/blog_mobile.html", {"post":bg})
	else:
		return render(response, "blog/blog_pc.html", {"post":bg})

def PostDetail(response,ur):
	bg=Post.objects.get(slug=ur)
	if response.user_agent.is_mobile == True:
		return render(response, "blog/blogpost_mobile.html", {"post":bg})
	else:
		return render(response, "blog/blogpost_pc.html", {"post":bg})