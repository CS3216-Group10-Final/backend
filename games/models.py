from django.db import models
from users.models import User


class Genre(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

    def __str__(self) -> str:
        return self.name

class Platform(models.Model):
    name = models.CharField(max_length=80, primary_key=True)

    def __str__(self) -> str:
        return self.name

class Game(models.Model):

    name = models.CharField(max_length=250)
    cover = models.CharField(max_length=250, blank=True)
    genres = models.ManyToManyField(Genre, related_name='games')
    platforms = models.ManyToManyField(Platform, related_name='games')

    def __str__(self) -> str:
        return self.name + self.genres.__str__()


class GameEntry(models.Model):
    class GameEntryStatus(models.IntegerChoices):
        WISHLIST = 0
        BACKLOG = 1
        PLAYING = 2
        COMPLETED = 3
        DROPPED = 4
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="game_entries")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="entries")
    rating = models.IntegerField(blank=True, null=True)
    review = models.TextField(blank=True)
    hours = models.IntegerField(blank=True, null=True)
    is_favourite = models.BooleanField(default=False)
    status = models.IntegerField(choices=GameEntryStatus.choices, default=3)
    time_started = models.DateTimeField(blank=True, null=True)
    time_completed = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.id.__str__() + ' ' + self.user.__str__() + ' ' + self.game.__str__()



