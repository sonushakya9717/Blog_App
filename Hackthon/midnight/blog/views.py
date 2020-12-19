from django.views import generic
from .models import Post
from django.shortcuts import render,HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User, auth 

def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def about(request):
    return render(request,'about.html')

def user_logout(request):
    return HttpResponseRedirect('/')

