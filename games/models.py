from django.db import models
from users.models import User

class Genre(models.Model):
    name = models.CharField(max_length=30)

class Platform(models.Model):
    name = models.CharField(max_length=50)

class Game(models.Model):
    name = models.CharField(max_length=250)
    #image = models.ImageField()
    genre = models.ManyToManyField(Genre)
    platform = models.ManyToManyField(Platform)

class GameEntry(models.Model):
    class GameEntryStatus(models.IntegerChoices):
        WISHLIST = 0
        BACKLOG = 1
        PLAYING = 2
        COMPLETED = 3
        DROPPED = 4
    user = models.ForeignKey(User)
    game = models.ForeignKey(Game)
    rating = models.IntegerField(blank=True)
    review = models.TextField(blank=True)
    hours = models.IntegerField(blank=True)
    is_favourite = models.BooleanField(default=False)
    status = models.IntegerField(choices=GameEntryStatus, default=3)
    time_started = models.DateTimeField(blank=True)
    time_completed = models.DateTimeField(blank=True)



