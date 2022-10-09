from django.apps import apps
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.db.models import Avg

class UserManager(BaseUserManager):
    """A custom model manager for the custom User model that uses email instead of username."""

    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """Creates and saves a User with the given username, email and password."""

        if not email:
            raise ValueError('Email must be given')
        if not username:
            raise ValueError('Username must be given')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email, password=None, **extra_fields):
        """Creates and saves a regular User with the given username, email and password."""

        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        """Creates and saves a Superuser with the given username, email and password."""
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    def profile_pic_image_path(instance, filename):
        return f'user/{instance.id}/{filename}'

    email = models.EmailField(unique=True)
    profile_picture_link = models.ImageField(upload_to=profile_pic_image_path, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def get_average_rating(self):
        return self.game_entries.aggregate(Avg('rating'))['rating__avg']

    def get_game_status_distribution(self):
        GameEntry = apps.get_model('games', 'GameEntry')
        game_entries = self.game_entries

        distribution = {}
        for status in GameEntry.GameEntryStatus:
            count = game_entries.filter(status=status).count()
            distribution[status] = count
        
        return distribution
    
    def get_game_genre_distribution(self):
        Genre = apps.get_model('games', 'Genre')
        game_entries = self.game_entries

        distribution = {}
        for genre in Genre.objects.all():
            count = game_entries.filter(game__genres=genre).count()
            distribution[genre] = count
        return distribution
    
    def get_platform_distribution(self):
        Platform = apps.get_model('games', 'Platform')
        game_entries = self.game_entries

        distribution = {}
        for platform in Platform.objects.all():
            count = game_entries.filter(game__platforms=platform).count()
            distribution[platform] = count
        return distribution