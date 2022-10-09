from platform import platform
from typing import Dict
from rest_framework import serializers
from .models import Game, GameEntry, Genre, Platform

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
    game_name = serializers.CharField(source='game.name')
    game_cover = serializers.CharField(source='game.cover')
    game_id = serializers.IntegerField(source='game.id')
    user_id = serializers.IntegerField(source='user.id')

    class Meta:
        model = GameEntry
        exclude = ['game', 'user']



