from django.apps import apps
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.db.models import Avg
from django.utils import timezone

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
    
    def generate_unique_username_from(self, username):
        result = username
        counter = 1
        while User.objects.filter(username=result):
            result = username + str(counter)
            counter += 1
        return result

class User(AbstractUser):
    def profile_pic_image_path(instance, filename):
        return f'user/{instance.id}/{filename}'

    email = models.EmailField(unique=True)
    profile_picture_link = models.ImageField(upload_to=profile_pic_image_path, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def get_average_rating(self):
        average_rating = self.game_entries.aggregate(Avg('rating'))['rating__avg']
        if not average_rating:
            return 0
        return average_rating

    def get_game_status_distribution(self):
        GameEntry = apps.get_model('games', 'GameEntry')
        game_entries = self.game_entries

        distribution = {}
        for status in GameEntry.GameEntryStatus:
            count = game_entries.filter(status=status).count()
            distribution[status] = count
        
        return distribution
    
    def get_game_genre_distribution(self):
        game_entries = self.game_entries
        distribution = {}
        for entry in game_entries.all():
            genres = entry.game.genres.all()
            for genre in genres:
                if genre in distribution:
                    distribution[genre] += 1
                else:
                    distribution[genre] = 1

        return distribution
    
    def get_platform_distribution(self):
        game_entries = self.game_entries
        distribution = {}
        for entry in game_entries.all():
            platforms = entry.platforms.all()
            for platform in platforms:
                if platform in distribution:
                    distribution[platform] += 1
                else:
                    distribution[platform] = 1

        return distribution
    
    def get_release_year_distribution(self):
        game_entries = self.game_entries
        distribution = {}
        for entry in game_entries.all():
            year = entry.game.first_release_date.year
            if year in distribution:
                distribution[year] += 1
            else:
                distribution[year] = 1

        return distribution

    def get_play_year_distribution(self):
        game_entries = self.game_entries
        distribution = {}
        for entry in game_entries.all():
            if not entry.time_started:
                continue

            start_year = entry.time_started.year
            end_year = entry.time_completed.year if entry.time_completed else timezone.now().year

            for year in range(start_year, end_year + 1):
                if year in distribution:
                    distribution[year] += 1
                else:
                    distribution[year] = 1

        return distribution