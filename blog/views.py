from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse
# Create your views here.

# posts= [ 
# 	{
# 		'author':'Lanre',
# 		'title':'Blog post 1',
# 		'content': 'First content post',
# 		'date_posted': 'August 5, 2019'

	
# 	},
# 	{
# 		'author':'Rizu',
# 		'title':'Blog post 2',
# 		'content': 'second content post',
# 		'date_posted': 'August 10, 2019'

	
# 	}
# ]

def home(request):
	context={
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html', context)
	#context can also be passed above

def about(request):
	return render(request, 'blog/about.html', {'title':'About'})