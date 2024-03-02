from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def index(request):
    posts = Post.objects.order_by('-pub_date')
    context = {'posts': posts}
    return render(request, 'bulletin/index.html', context)

def post(request, id):
    post = get_object_or_404(Post, id__startswith=id)
    context = {'post': post}
    return render(request, 'bulletin/post.html', context)