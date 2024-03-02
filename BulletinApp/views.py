from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import *
from django.contrib.auth import authenticate
from geopy.distance import geodesic

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
        CustomUser.objects.create_user(first_name = firstName, last_name=lastName, email = email, password=password, username=email)
    return HttpResponseRedirect(reverse('bulletin:index'))

def login(request):
    return render(request, 'bulletin/login')

def loginUser(request):
    try:
        email = request.POST['email']
        password = request.POST['password']
    except (KeyError, User.DoesNotExist):
        return
    else:
        user = authenticate(username=email, password=password)
    if user is not None:
        return HttpResponseRedirect(reverse('bulletin:index'))
    else:
        return HttpResponseRedirect(reverse('bulletin:login'))


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

def explore(request, distance):
    # Retrieve the current user
    current_user = request.user

    # Get the user's location
    user_location = (current_user.latitude, current_user.longitude)

    # Calculate distances and filter bulletin boards
    bulletin_boards = []
    for bulletin in Bulletin.objects.all():
        # Get bulletin board location
        bulletin_location = (bulletin.latitude, bulletin.longitude)
        
        # Calculate distance from user to bulletin board
        bulletin_distance = geodesic(user_location, bulletin_location).miles
        
        # Check if distance is within the specified range
        if bulletin_distance <= distance:
            bulletin_boards.append((bulletin, bulletin_distance))

    # Sort bulletin boards by distance
    bulletin_boards.sort(key=lambda x: x[1])

    # Pass the sorted list of bulletin boards to the template
    context = {
        'bulletin_boards': bulletin_boards,
    }

    return render(request, 'explore.html', context) 