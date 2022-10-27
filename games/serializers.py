from platform import platform
from typing import Dict
from rest_framework import serializers
from .models import Game, GameEntry, Genre, Platform
from users.models import User

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class GameEntrySerializer(serializers.ModelSerializer):
    game_name = serializers.CharField(source='game.name', read_only=True)
    game_cover = serializers.CharField(source='game.cover', read_only=True)
    game_id = serializers.PrimaryKeyRelatedField(source='game', queryset = Game.objects.all())
    user_id = serializers.PrimaryKeyRelatedField(source='user', queryset = User.objects.all())

    class Meta:
        model = GameEntry
        exclude = ['game', 'user']

class ReviewSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    user_picture = serializers.ImageField(
        source='user.profile_picture_link',
        use_url=True, 
        required=False, 
        allow_empty_file=True,
        allow_null=True)
    game_id = serializers.PrimaryKeyRelatedField(source='game', queryset = Game.objects.all())

    class Meta:
        model = GameEntry
        fields = ['user_username', 'user_picture', 'game_id', 'rating', 'review']
