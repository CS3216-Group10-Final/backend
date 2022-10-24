from django.db import models
from games.models import Game, GameEntry
from users.models import User


class Activity(models.Model):
    class ActivityType(models.IntegerChoices):
        NEW_STATUS = 0
        NEW_RATING = 1
        NEW_REVIEW = 2
        NEW_GAME = 3
        #steam activities:

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activities")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="activities")
    game_entry = models.ForeignKey(GameEntry, on_delete=models.CASCADE, related_name="activities")
    activity_type = models.IntegerField(choices=ActivityType.choices)
    time_created = models.DateTimeField(auto_now_add=True)
    new_status = models.IntegerField(choices=GameEntry.GameEntryStatus.choices, blank=True, null=True)  
    new_rating = models.PositiveSmallIntegerField(blank=True, null=True)
    new_review = models.TextField(blank=True)
    

    def __str__(self) -> str:
        return self.user.__str__() + ' ' + self.game.__str__() + ' ' + self.activity_type.__str__()

    def generateActivities(new_entry, user, original_status, original_rating, original_review, *args, **kwargs):

        if original_status is None:
            a = Activity(user=new_entry.user, game=new_entry.game, activity_type=Activity.ActivityType.NEW_GAME.value,
            new_status=new_entry.status, game_entry=new_entry)
            a.save()
        elif original_status != new_entry.status:
            a = Activity(user=new_entry.user, game=new_entry.game, activity_type=Activity.ActivityType.NEW_STATUS.value,
            new_status=new_entry.status, game_entry=new_entry)
            a.save()
        
        if original_rating != new_entry.rating:
            a = Activity(user=new_entry.user, game=new_entry.game, activity_type=Activity.ActivityType.NEW_RATING.value,
            new_rating=new_entry.rating, game_entry=new_entry)
            a.save()

        if original_review != new_entry.review:
            a = Activity(user=new_entry.user, game=new_entry.game, activity_type=Activity.ActivityType.NEW_REVIEW.value,
            new_review=new_entry.review, game_entry=new_entry)
            a.save()
