from django.db import models
from games.models import Game, GameEntry
from users.models import User


class Activity(models.Model):
    class ActivityType(models.IntegerChoices):
        NEW_STATUS = 0
        NEW_RATING = 1
        NEW_REVIEW = 2
        #steam activities:

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activities")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="activities")
    activity_type = models.IntegerField(choices=ActivityType.choices)
    time_created = models.DateTimeField(auto_now_add=True)
    new_status = models.IntegerField(choices=GameEntry.GameEntryStatus, blank=True, null=True)  
    new_rating: models.PositiveSmallIntegerField(blank=True, null=True)
    new_review: models.TextField(blank=True)
    

    def __str__(self) -> str:
        return self.user.__str__() + ' ' + self.game.__str__() + ' ' + self.activity_type.__str__()
