from django.db import models

from users.models import User

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="outgoing_follows")
    followee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="incoming_follows")
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.follower} follows {self.followee}'
    
    @classmethod
    def get_followers_of(cls, user):
        return User.objects.filter(outgoing_follows__followee=user)
    
    @classmethod
    def get_followees_of(cls, user):
        return User.objects.filter(incoming_follows__follower=user)