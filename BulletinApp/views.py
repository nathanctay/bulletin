from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import *
from django.contrib.auth import authenticate
from geopy.distance import geodesic
from django.contrib.auth import logout
from .forms import *


# Create your views here.
def index(request):
    user = request.user
    posts = Post.objects.order_by('-pub_date')
    bulletins = user.bulletin_list.all()
    print(user)
    context = {'bulletins' : bulletins, 'posts': posts, 'user':user}
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
    logout(request)
    return render(request, 'bulletin/login.html')


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

def bulletin(request, id):
    user = request.user
    bulletin = get_object_or_404(Bulletin, id__startswith=id)
    bulletins = user.bulletin_list.all()
    members = bulletin.users.all()
    posts = Post.objects.filter(bulletin=bulletin)
    context = {'bulletins': bulletins, 'posts': posts, 'bulletin': bulletin, 'members': members}
    return render(request, 'bulletin/bulletin.html', context)

def post(request, id):
    user = request.user
    bulletins = user.bulletin_list.all()
    post = get_object_or_404(Post, id__startswith=id)
    bulletin = post.bulletin
    members = bulletin.users.all()
    # print(members)
    print(bulletin)
    comments = Comment.objects.filter(post=post)
    context = {'bulletins': bulletins, 'bulletin': bulletin, 'post': post, 'comments': comments,'members': members}
    return render(request, 'bulletin/post.html', context)

def comment(request, id):
    user = request.user
    post = get_object_or_404(Post, id__startswith=id)
    try:
        content = request.POST['content']
    except (KeyError, Comment.DoesNotExist):
        return
    else:
        Comment(creator = user, content = content, post = post, pub_date = timezone.now()).save()
        return HttpResponseRedirect(reverse(f'bulletin:post', args=(id,)))
    

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

def bulletinEdit(request, bulletinId = None):
    user = request.user
    bulletins = user.bulletin_list.all()

    if bulletinId is not None:
        bulletin = Bulletin.objects.get(id = bulletinId)
        initial_form = {"bulletin_name": bulletin.title, "description": bulletin.description, 'bulletin_picture': bulletin.bulletin_picture}
    else:
        initial_form = {"bulletin_name": '', "description": '', 'bulletin_picture': ''}
    

    if request.method == "POST":
        
    # else:
        # context[initial_list] = [{"bulletin_name": '', "description": '',}]
        form = BulletinForm(request.POST, request.FILES, initial=initial_form)
        if form.is_valid():
            name = form.cleaned_data.get("bulletin_name")
            description = form.cleaned_data.get("description")
            bulletin_picture = form.cleaned_data.get("pic_field")
            bulletin = Bulletin.objects.create(creator = user, title = name,bulletin_picture = bulletin_picture, description = description,  latitude = 0, longitude = 0, )
            bulletin.users.add(user)
            bulletin.save()
    else:
        form = BulletinForm(initial=initial_form)

    context = {'bulletins' : bulletins, 'user':user, 'form': form}
    
    
    return render(request, 'bulletin/bulletin-edit.html', context)

def saveBulletin(request):
    user = request.user
    if request.method == "POST":
        form = BulletinForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            description = form.cleaned_data.get("description")
            bulletin_picture = form.cleaned_data.get("pic_field")
            Bulletin.objects.create(creator = user, title = name,bulletin_picture = bulletin_picture, description = description,  latitude = 0, longitude = 0).save()
    else:
        form = BulletinForm()
    return 