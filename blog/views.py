from django.shortcuts import render
from .models import post
#from django.http import HttpResponse

# Create your views here.
def index(request):
    posts= post.objects.all()
    return render(request, 'blog/index.html',{'posts': posts})
 #HttpResponse('<h1 style="color:red">Index page </h1>')

#ef about(request):
#    return # HttpResponse('<h1 style="color:blue">About page </h1>')