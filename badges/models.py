from django.db import models

from users.models import User

class Badge(models.Model):
    def badge_pic_image_path(instance, filename):
        return f'badge/{instance.id}/{filename}'

    name = models.CharField(max_length=250)
    picture = models.ImageField(upload_to=badge_pic_image_path)
    description = models.TextField()

    def __str__(self):
        return self.name

class BadgeEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="badge_entries")
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE, related_name="entries")
    time_achieved = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} {self.user} {self.badge}'
