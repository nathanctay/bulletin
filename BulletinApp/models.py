from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class Bulletin(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    bulletin = models.ForeignKey(Bulletin, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    description = models.TextField()
    event_date_time = models.DateTimeField()
    guestlist = models.ManyToManyField(User, related_name='events_attending')

    def __str__(self):
        return self.title
    



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.content[:45]
    

