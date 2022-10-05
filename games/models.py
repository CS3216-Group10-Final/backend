from django.db import models
from pb_model.models import ProtoBufMixin
from displaycase import igdbapi_pb2
#from users.models import User

class Genre(models.Model):
    name = models.CharField(max_length=30)

class Platform(models.Model):
    name = models.CharField(max_length=50)

class Game(ProtoBufMixin, models.Model):
    pb_model = igdbapi_pb2.Game

    name = models.CharField(max_length=250)
    #image = models.ImageField()
    #genre = models.ManyToManyField(Genre)
    #platform = models.ManyToManyField(Platform)

    def __str__(self) -> str:
        return self.name

class GameEntry(models.Model):
    class GameEntryStatus(models.IntegerChoices):
        WISHLIST = 0
        BACKLOG = 1
        PLAYING = 2
        COMPLETED = 3
        DROPPED = 4
    #user = models.ForeignKey(User)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    rating = models.IntegerField(blank=True)
    review = models.TextField(blank=True)
    hours = models.IntegerField(blank=True)
    is_favourite = models.BooleanField(default=False)
    status = models.IntegerField(choices=GameEntryStatus.choices)
    time_started = models.DateTimeField(blank=True)
    time_completed = models.DateTimeField(blank=True)



