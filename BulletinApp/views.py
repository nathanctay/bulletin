from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import *

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-pub_date')
    context = {'posts': posts}
    return render(request, 'bulletin/index.html', context)

def register(request):

    return render(request, 'bulletin/register.html')

def registerUser(request):
    try:
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
    except (KeyError, User.DoesNotExist):
        return
    else:
        User.objects.create_user(firstName, email, password)
    return HttpResponseRedirect(reverse('bulletin:index'))

def login(request):
    return render(request, 'bulletin/login')

def post(request, id):
    post = get_object_or_404(Post, id__startswith=id)
    comments = Comment.objects.filter(post=post)
    context = {'post': post, 'comments': comments}
    return render(request, 'bulletin/post.html', context)

def comment(request, id):
    post = get_object_or_404(Post, id__startswith=id)
    try:
        commenter = request.POST['commenter']
        content = request.POST['content']
    except (KeyError, Comment.DoesNotExist):
        return
    else:
        Comment()