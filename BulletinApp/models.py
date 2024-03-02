from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    email = models.EmailField(unique=True)    
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    # Add more fields as needed

    def save(self, *args, **kwargs):
        # Set the username to be the email address
        self.username = self.email
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name 

class Bulletin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)
    bulletin_picture = models.ImageField(upload_to='bulletin_pictures/')
    description = models.CharField(max_length=500, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    users = models.ManyToManyField(CustomUser, related_name="bulletin_list")

    def __str__(self):
        return self.title
        
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    bulletin = models.ForeignKey(Bulletin, on_delete=models.CASCADE)
    post_picture = models.ImageField(upload_to='post_pictures/')
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    description = models.TextField()
    event_date_time = models.DateTimeField()
    guestlist = models.ManyToManyField(CustomUser, related_name='events_attending')

    def __str__(self):
        return self.title
    

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.content[:45]
    

